from abc import ABC, abstractmethod


class EmailRepository(ABC):

    @abstractmethod
    def send_email(self, to_emails: list, cc_emails:list, subject, body, attachments=()) -> None:
        pass
