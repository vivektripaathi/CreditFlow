from django.apps import AppConfig



class LoanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loan'
    inject_container = None
    
    def ready(self):
        from loan.inject import LoanConainter
        import loan

        self.inject_container = LoanConainter()
        self.inject_container.wire(
            packages=[loan],
            modules=[],
        )

