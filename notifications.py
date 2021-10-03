from definitions import *

class Notifications:
    def __init__(self, font_size = 24):
        self.current_msg, self.msg_timer, self.msg_expiry = '', 0, MSG_EXPIRY

        self.text_start_x, self.text_start_y = 0, 0 

        self.font_size = font_size
        self.font = GET_SIZED_FONT(self.font_size)
        self.rendered_text = self.font.render("", True, WHITE)
        self.line_h = self.rendered_text.get_rect().h

        self.vpad = 5
        self.lines = []

    def render_text(self):
        self.rendered_text = self.font.render(self.current_msg, True, WHITE)
        self.lines = []
        for i, line in enumerate(self.current_msg.split('\n')):
            rendered_line = self.font.render(line, True, WHITE)
            textRect = rendered_line.get_rect()
            textRect.center = ( self.text_start_x + textRect.w // 2, 
                self.text_start_y + i * (self.font_size + self.vpad))
            self.lines += [(rendered_line, textRect)]

    def update(self, dt):
        if self.msg_timer > self.msg_expiry:
            self.current_msg = ''
            self.msg_timer = 0
            self.render_text()
        else:
            self.msg_timer += dt

    def post(self, msg, x = 0, y = 0, align_bot = False, time = MSG_EXPIRY):
        self.text_start_x, self.text_start_y = x, y
        if align_bot:
            lines = msg.count('\n') + 1
            self.text_start_y -= \
                (lines) * (self.line_h + self.vpad)
        self.current_msg, self.msg_timer, self.msg_expiry = msg, 0, time
        self.render_text()

    def draw(self, surf):
        if self.current_msg != '':
            for line_info in self.lines:
                surf.blit(*line_info)
