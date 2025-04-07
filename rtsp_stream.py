import cv2
import yaml
import sys

def load_config(config_file="config.yaml"):
    try:
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)

def main():
    config = load_config()
    rtsp_config = config.get('rtsp', {})
    
    username = rtsp_config.get('username', 'your_username')
    password = rtsp_config.get('password', 'your_password')
    ip_address = rtsp_config.get('ip_address', '192.168.1.100')
    port = rtsp_config.get('port', '554')
    stream_path = rtsp_config.get('stream_path', 'live')

    rtsp_url = f"rtsp://{username}:{password}@{ip_address}:{port}/{stream_path}"

    cap = cv2.VideoCapture(rtsp_url)
    if not cap.isOpened():
        print("Error: Could not open RTSP stream. Check URL, credentials, or network.")
        sys.exit(1)

    cap.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, 5000)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to retrieve frame. Stream may have ended or connection lost.")
            break

        cv2.imshow("RTSP Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Stream closed.")

if __name__ == "__main__":
    main()