import configparser

file = open("Configuration/config.ini","r")
config = configparser.RawConfigParser(allow_no_value=True)
config.read_file(file)

class ReadProperties:
    @staticmethod
    def get_broken_link_url():
        url = config.get('common_info', 'broken_image_url')
        return url

    @staticmethod
    def get_file_upload_url():
        url = config.get('common_info', 'file_upload_url')
        return url

    @staticmethod
    def get_login_url():
        url = config.get('common_info', 'from_authentication')
        return url

    @staticmethod
    def get_alert_url():
        url = config.get('common_info', 'java_script_alert')
        return url

    @staticmethod
    def get_drop_down_url():
        url = config.get('common_info', 'drop_down')
        return url


