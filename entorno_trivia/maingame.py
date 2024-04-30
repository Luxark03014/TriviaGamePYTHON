import pygame
import json
import sys
import xml.etree.ElementTree as ET
from pygame import mixer



def save_results_to_xml(results, total_correct, filepath):
    root = ET.Element("resultados")
    for result in results:
        result_elem = ET.SubElement(root, "resultado")
        ET.SubElement(result_elem, "pregunta").text = result['pregunta']
        ET.SubElement(result_elem, "eleccionUsuario").text = result['eleccionUsuario']
        ET.SubElement(result_elem, "correcta").text = str(result['correcta']).lower()
    score_elem = ET.SubElement(root, "puntuacionTotal")
    score_elem.text = str(total_correct)
    tree = ET.ElementTree(root)
    tree.write(filepath)

def save_results_to_json(results, filepath):
    with open(filepath, 'w') as file:
        json.dump(results, file, indent=4)

def init_pygame():
    pygame.init()
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Trivia Game")
    return screen

def load_questions_from_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data['preguntas']

def draw_text(text, font, color, screen, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

def render_question(question, screen, font):
    backgroundPREGUNTAS = pygame.image.load('background.jpg')
    screen.fill((0, 0, 0))
    screen.blit(backgroundPREGUNTAS, (0, 0))
    y_pos = 50
    draw_text(question['Enunciado'], font, (255, 255, 255), screen, 50, y_pos)
    y_pos += 50
    for i in range(1, 5):
        draw_text(f"{i}. {question[f'Respuesta{i}']}", font, (255, 255, 255), screen, 50, y_pos)
        y_pos += 30
    pygame.display.flip()

def start_screen(screen):
    y_pos = 50
    font = pygame.font.Font(None, 50)
   
    button_font = pygame.font.Font(None, 36)
    start_button = pygame.Rect(300, 400, 200, 60)
    running = True
    backgroundINICIO = pygame.image.load('INICIO.jpg')
    
    while running:
        screen.fill((0, 0, 0))
        screen.blit(backgroundINICIO, (0, 0))
        draw_text(' BIENVENIDO AL CONCURSO DE PREGUNTAS', font, (255, 255, 255), screen, 10, y_pos)
        pygame.draw.rect(screen, (30, 144, 255), start_button)  
        draw_text("Iniciar", button_font, (255, 255, 255), screen, 340, 410)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    running = False

def final_result(results, total_correct, screen, font):
    screen.fill((0, 0, 0))
    save_results_to_json(results, 'resultados.json')
    save_results_to_xml(results, total_correct, 'resultados.xml')
    y_pos = 50
    draw_text('RESULTADO FINAL:', font, (255, 255, 255), screen, 50, y_pos)
    y_pos = 100
    draw_text(f"TOTAL DE RESPUESTAS CORRECTAS: {total_correct}", font, (255, 255, 255), screen, 50, y_pos)
    pygame.display.flip()
    pygame.time.wait(5000)

def run_game():
    screen = init_pygame()
    font = pygame.font.Font(None, 25)
    start_screen(screen)
    questions = load_questions_from_json('preguntas.json')
    current_question = 0
    total_correct = 0
    game_results = []

    running = True
    while running:
        if current_question < len(questions):
            render_question(questions[current_question], screen, font)
        else:
            final_result(game_results, total_correct, screen, font)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                if current_question < len(questions):
                    index = event.key - pygame.K_1
                    selected_answer = f'Respuesta{index+1}'
                    correct = selected_answer == questions[current_question]['RespuestaCorrecta']
                    total_correct += int(correct)
                    result = {
                        "pregunta": questions[current_question]["Enunciado"],
                        "eleccionUsuario": questions[current_question][selected_answer],
                        "correcta": correct
                    }
                    game_results.append(result)
                    current_question += 1

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
