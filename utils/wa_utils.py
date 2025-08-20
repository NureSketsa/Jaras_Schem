import pyautogui
import datetime

error_images: dict[str, str] = {
    "error_check/error_number_invalid.png": "Number not registered on WhatsApp.",
    "error_check/error_loading.png": "WhatsApp failed to load properly.",
    "error_check/error_starting_chat.png": "WhatsApp failed to start the chat.",
}

def detect_whatsapp_error(file_name: str, confidence: float = 0.8, grayscale: bool = True) -> str:
    for path, message in error_images.items():
        try:
            if pyautogui.locateOnScreen(path, confidence = confidence, grayscale = grayscale):
                return f"{file_name} | ⚠️ Error - {message}"
        except pyautogui.ImageNotFoundException:
            continue
        except Exception as e:
            print(f"Unexpected error checking {path}: {e}")
            continue
    
    path: str = "error_check/success_no_draft.png"

    try:
        if pyautogui.locateOnScreen(path, confidence=confidence, grayscale=grayscale):
            return f"{file_name} | Success - Message sent or in progress."
    except pyautogui.ImageNotFoundException:
        return f"{file_name} | ⚠️ Error - Draft message not sent."
    except Exception as e:
        print(f"Unexpected error checking {path}: {e}")
    return f"{file_name} | ⚠️ Error - Unable to determine status."


def fixNumber(s: str):
    s = s.strip()
    if s.startswith('0'):
        s = '+62' + s[1:]
    elif s.startswith('62'):
        s = '+' + s
    elif s.startswith('8'):
        s = "+62" + s
    return s


log_file: str = "output/wa_log.txt"

def log_status(number: str, status: str):
    print(f"sent to {number} — {status}")
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {number} — {status}\n")
