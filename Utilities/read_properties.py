import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadProperties:
    @staticmethod
    def get_broken_link_url():
        url = config.get('common info', 'broken_image_url')
        return url

    @staticmethod
    def get_file_upload_url():
        url = config.get('common info', 'file_upload_url')
        return url

    @staticmethod
    def get_login_url():
        url = config.get('common info', 'from_authentication')
        return url

    @staticmethod
    def get_alert_url():
        url = config.get('common info', 'java_script_alert')
        return url

    @staticmethod
    def get_drop_down_url():
        url = config.get('common info', 'drop_down')
        return url


