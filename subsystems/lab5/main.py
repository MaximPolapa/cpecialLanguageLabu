import pygame
import math
import colorsys
import logging

def main():
    # Initialize Pygame
    pygame.init()

    # Define basic colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Screen dimensions
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

    # Set up Pygame screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('3D Shapes')
    clock = pygame.time.Clock()

    # Donut settings
    A, B = 0, 0  # rotation angles for the donut
    center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    scale = 200  # Scale factor for the donut size
    char_set = ".,-~:;=!*#$@"  # Luminance characters
    font_style = pygame.font.SysFont('Arial', 18, bold=True)
    hue_shift = 0  # For color cycling

    # Define the render functions
    def render_parallelepiped(angle_x, angle_y, angle_z, vertices, scale, offset_x, offset_y):
        projected_vertices = []
        for v in vertices:
            x, y, z = v
            y, z = y * math.cos(angle_x) - z * math.sin(angle_x), y * math.sin(angle_x) + z * math.cos(angle_x)
            x, z = x * math.cos(angle_y) - z * math.sin(angle_y), x * math.sin(angle_y) + z * math.cos(angle_y)
            x, y = x * math.cos(angle_z) - y * math.sin(angle_z), x * math.sin(angle_z) + y * math.cos(angle_z)
            projected_x = int(x * scale) + offset_x
            projected_y = int(y * scale) + offset_y
            projected_vertices.append((projected_x, projected_y))
        for i in range(4):
            pygame.draw.line(screen, WHITE, projected_vertices[i], projected_vertices[(i + 4) % 8], 1)
            pygame.draw.line(screen, WHITE, projected_vertices[i], projected_vertices[(i + 1) % 4], 1)
            pygame.draw.line(screen, WHITE, projected_vertices[i + 4], projected_vertices[(i + 1) % 4 + 4], 1)

    def render_donut(center_x, center_y, scale, A, B, hue_shift):
        screen.fill(BLACK)
        z_buffer = [0] * (SCREEN_WIDTH * SCREEN_HEIGHT)  # Z-buffer for depth calculation
        screen_buffer = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]  # Screen buffer
        phi_spacing = 2
        theta_spacing = 2

        # Calculate donut points
        for theta in range(0, 628, theta_spacing):
            for phi in range(0, 628, phi_spacing):
                c = math.sin(phi)
                d = math.cos(theta)
                e = math.sin(A)
                f = math.sin(theta)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(phi)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int(center_x + scale * D * (l * h * m - t * n))  # 3D x coordinate after transformation
                y = int(center_y + scale * D * (l * h * n + t * m))  # 3D y coordinate after transformation
                z = int(D * scale)
                o = int(x + SCREEN_WIDTH * y)  # 1D screen coordinate
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # Luminance index
                
                # Update buffers if this point is closer to the viewer than what's already plotted
                if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT and z > z_buffer[o]:
                    z_buffer[o] = z
                    screen_buffer[y][x] = char_set[N if N > 0 else 0]

        # Draw the screen buffer to the Pygame window
        for y, row in enumerate(screen_buffer):
            for x, char in enumerate(row):
                if char != ' ':
                    hsv = (hue_shift % 1, 1, 1)  # Hue, saturation, value
                    color = pygame.Color(0)
                    color.hsva = (hue_shift % 360, 100, 100)  # Convert HSV to RGB
                    text_surface = font_style.render(char, True, color)
                    screen.blit(text_surface, (x, y))

        hue_shift += 1  # Increment hue shift for the next frame to change colors over time
        return hue_shift

    # Get user input
    shape_choice = input("Choose a shape:\n1 - Parallelepiped\n2 - Donut\nEnter number: ")

    # Parallelepiped settings
    vertices = [
        [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
        [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]
    ]
    scale = 100
    offset_x, offset_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    angle_x, angle_y, angle_z = 0, 0, 0

    # Donut settings
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    donut_scale = 200
    char_set = ".,-~:;=!*#$@"
    font_style = pygame.font.SysFont('Arial', 18, bold=True)
    hue_shift = 0  # Initialize hue shift for donut color

    # Main loop
    running = True
    while running:
        screen.fill(BLACK)

        if shape_choice == '1':
            # Render parallelepiped
            angle_x += 0.01
            angle_y += 0.01
            angle_z += 0.01
            render_parallelepiped(angle_x, angle_y, angle_z, vertices, scale, offset_x, offset_y)
        elif shape_choice == '2':
            # Render donut
            A += 0.07  # Increment the rotation angle A for the donut
            B += 0.03  # Increment the rotation angle B for the donut
            hue_shift = render_donut(center_x, center_y, donut_scale, A, B, hue_shift)
        else:
            print("Invalid choice. Exiting.")
            logging.info("ERROR invalid choice")
            running = False

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type is pygame.QUIT or (event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE):
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
