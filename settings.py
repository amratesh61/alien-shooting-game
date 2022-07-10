class Settings:
    def __init__(self):
        self.bg_color=(255,255,255)
        self.screen_width = 1000
        self.screen_height =800
        self.ship_speed_factor = 1
        self.bullets_allowed = 7
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.alien_speed_factor = 8
        self.fleet_drop_speed = 3
 # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 2
        self.shift_limit = 2
        self.speedup_scale = 2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.alien_points = 10

        self.bullet_speed_factor = 3
        self.alien_speed_factor = 3
        self.fleet_direction = 1
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self.alien_points
