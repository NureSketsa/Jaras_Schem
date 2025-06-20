import pyautogui

error_images = {
    "images_invalid/error_number_invalid.png": "Number not registered on WhatsApp.",
    "images_invalid/error_loading.png": "WhatsApp failed to load properly.",
    "images_invalid/error_starting_chat.png": "WhatsApp failed to start the chat."
}

def detect_whatsapp_error(File_name,confidence=0.8, grayscale=True):
    """
    Scan screen for known WhatsApp error images.
    Returns status message based on detection.
    """
    for path, message in error_images.items():
        try:
            if pyautogui.locateOnScreen(path, confidence=confidence, grayscale=grayscale):
                return f"{File_name} | ⚠️ Error - {message}"
        except pyautogui.ImageNotFoundException:
            continue
        except Exception as e:
            print(f"Unexpected error checking {path}: {e}")
            continue

    return f"{File_name} | Success - Message sent or in progress."


def fixNumber(s : str) :
    s = s.strip()
    if s.startswith('0'):
        s = '+62' + s[1:]
    elif s.startswith('62'):
        s = '+' + s
    elif s.startswith('8') :
        s = "+62" + s
    return s
