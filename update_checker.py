class UpdateChecker:
    def __init__(self):
        self.current_version = "v1.0.0"
        self.last_update_date = "20/2/2024"
        self.update_available = False
        self.latest_version = "v1.1.0"
        self.update_file_size = "150 MB"

    def check_updates(self):
        # Simulate checking for updates
        self.update_available = False
        return self.update_available

    def get_update_status(self):
        if self.update_available:
            return f"- Update available: {self.latest_version}\n\n- Please download the update."
        else:
            return f"- Last update: {self.last_update_date}\n\n- All is up to date."

    def get_release_notes(self):
        if self.update_available:
            return f"\t\tWhat’s New in {self.latest_version}?\n\n- Release Notes: \n\n\tBug fixes\n\tImproved Driver Monitoring System\n\tCan Open Songs from any tab\n\n- File Size: 150 MB"
        else:
            return f"- All is up to date."


    def apply_updates(self):
        if self.update_available:
            return f"Applying Updates"
        else:
            return f"No Updates to download"
