from GameLogic import *

# Initialize Font Module.
pygame.font.init()

# Saves The Highest User Score From The Leaderboard File.
top, index = top_scores()
top = top[index[0]]

# Title Of The Application Being Executed.
pygame.display.set_caption('Blocks')


# Main Game Driving Function.
def main():
    # Set The Game Screen & Update The Dimensions.
    background = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.update()

    # Initialize The Run Variable For The While Loop To Be True & The Variable Call For The Next Piece To Be False.
    run = True
    load_piece = False
    # Initialize The Variable Representing Current User Line & Score.
    lines = 0
    score = 0
    # Initialize The Dictionary Used To Keep Track of Piece Position.
    previous_position = {}
    # Initialize Variables Representing The Initial Piece & The Following Two Pieces.
    current_piece = get_piece()
    next_piece = get_piece()
    next_piece_2 = get_piece()
    # Initialize The Time Module To A Variable.
    clock = pygame.time.Clock()
    # Set The Initial Time To Zero & The Piece Speed To A Constant At First.
    fall_time = 0
    piece_speed = 0.3

    while run:

        grid = update_grid(previous_position)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > piece_speed:
            fall_time = 0
            current_piece.y += 1
            if not (check_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                load_piece = True

        # Loop Used To Exit The Program Per User Request.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            # Check If A Key Has Been Held Down.
            if event.type == pygame.KEYDOWN:
                # When The Up Key Is Pressed, The Piece Will Rotate Through All Available Options.
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (check_space(current_piece, grid)):
                        current_piece.rotation -= 1
                # When The Down Key Is Pressed, The Piece Will Drop One Block Down.
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (check_space(current_piece, grid)):
                        current_piece.y -= 1
                # When The Left Key Is Pressed, The Piece Will Move One Block To The Left.
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (check_space(current_piece, grid)):
                        current_piece.x += 1
                # When The Right Key Is Pressed, The Piece Will Move One Block To The Right.
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (check_space(current_piece, grid)):
                        current_piece.x -= 1
                # When The Space Bar Is Pressed, The Piece Will Hard Drop All The Way Down.
                if event.key == pygame.K_SPACE:
                    while check_space(current_piece, grid):
                        current_piece.y += 1
                    current_piece.y -= 1

        # Initialize The Variable Representing The Current Piece Shape.
        piece_position = piece_format_reader(current_piece)
        # Add The X & Y Values For The Current Piece Into The Grid.
        for i in range(len(piece_position)):
            x, y = piece_position[i]
            if y > -1:
                grid[y][x] = current_piece.color
        # When The Piece Reaches The Bottom Layer...
        if load_piece:
            for position in piece_position:
                a = (position[0], position[1])
                previous_position[a] = current_piece.color
            # Set Current Piece To The Next Piece.
            current_piece = next_piece
            # Set Next Piece To The Second Next Piece.
            next_piece = next_piece_2
            # Load Another Piece & Set It To The Second Next Piece.
            next_piece_2 = get_piece()
            # Set Load / Change Of Piece To False.
            load_piece = False
            # Check If One Or More Lines Were Cleared & If So, How Many Lines Were Cleared.
            lines += row_completed(grid, previous_position)

        # Call Which Returns The Score & Speed Given The Current Level.
        score, piece_speed = level(lines, score, piece_speed)
        # Call Which Draws The Grid Lines & Other Contents To The User.
        draw_background(background, grid, score, top, lines)
        # Call Which Displays The Two Next Pieces To The User.
        display_next_piece(next_piece, next_piece_2, background)
        # Update The Display With New Data.
        pygame.display.update()

        # When The Game Loss Function returns True. Show End Screen And Request UserName For LeaderBoard.
        if game_loss(previous_position):
            pygame.display.update()
            text = user_input()
            pygame.time.delay(1300)
            run = False
            write(score, text)


# Function Used To Call Menu ( LeaderBoard ) & The Start Of The Game
def main_menu():
    run = True
    while run:
        leader_board()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.display.quit()


# Calling The Beginning Of The Game.
main_menu()
