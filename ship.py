import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船并设置初始化位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen.bottom

    def blitme(self):
        """在指定位置显示飞船"""
        self.screen.blit(self.image, self.rect)