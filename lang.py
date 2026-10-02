# -*- coding: utf-8 -*-
LANGS = {"pt": "Português (BR)", "es": "Español", "en": "English"}

T = {
 "app_title": {"pt": "BT3 Effect Studio", "es": "BT3 Effect Studio", "en": "BT3 Effect Studio"},
 "file": {"pt": "Arquivo", "es": "Archivo", "en": "File"},
 "open": {"pt": "Abrir .pak...", "es": "Abrir .pak...", "en": "Open .pak..."},
 "save": {"pt": "Salvar", "es": "Guardar", "en": "Save"},
 "save_as": {"pt": "Salvar como...", "es": "Guardar como...", "en": "Save as..."},
 "undo": {"pt": "Desfazer", "es": "Deshacer", "en": "Undo"},
 "quit": {"pt": "Sair", "es": "Salir", "en": "Quit"},
 "language": {"pt": "Idioma", "es": "Idioma", "en": "Language"},
 "templates": {"pt": "Modelos", "es": "Modelos", "en": "Templates"},
 "no_templates": {"pt": "(coloque .pak na pasta 'modelos')", "es": "(pon .pak en la carpeta 'modelos')", "en": "(put .pak files in the 'modelos' folder)"},
 "help": {"pt": "Ajuda", "es": "Ayuda", "en": "Help"},
 "about": {"pt": "Sobre", "es": "Acerca de", "en": "About"},
 "about_text": {"pt": "BT3 Effect Studio v0.1\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.1\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.1\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "no_file": {"pt": "Nenhum efeito aberto", "es": "Ningún efecto abierto", "en": "No effect open"},
 "summary": {"pt": "{n} mini-efeitos · {c} categorias · {f} arquivos", "es": "{n} mini efectos · {c} categorías · {f} archivos", "en": "{n} mini-effects · {c} categories · {f} files"},
 "col_chk": {"pt": "✓", "es": "✓", "en": "✓"},
 "col_idx": {"pt": "#", "es": "#", "en": "#"},
 "col_type": {"pt": "Tipo", "es": "Tipo", "en": "Type"},
 "col_group": {"pt": "Grupo", "es": "Grupo", "en": "Group"},
 "col_tex": {"pt": "DBT/Tex", "es": "DBT/Tex", "en": "DBT/Tex"},
 "col_inv": {"pt": "Invocação", "es": "Invocación", "en": "Invoke"},
 "col_size": {"pt": "Tamanho", "es": "Tamaño", "en": "Size"},
 "col_color": {"pt": "Cor", "es": "Color", "en": "Color"},
 "mark_all": {"pt": "Marcar todos", "es": "Marcar todos", "en": "Check all"},
 "unmark_all": {"pt": "Desmarcar todos", "es": "Desmarcar todos", "en": "Uncheck all"},
 "mark_group": {"pt": "Marcar grupo:", "es": "Marcar grupo:", "en": "Check group:"},
 "remove_marked": {"pt": "Remover marcados", "es": "Eliminar marcados", "en": "Remove checked"},
 "tab_colors": {"pt": "Cores", "es": "Colores", "en": "Colors"},
 "tab_params": {"pt": "Tamanho e tempo", "es": "Tamaño y tiempo", "en": "Size & timing"},
 "tab_groups": {"pt": "Grupos", "es": "Grupos", "en": "Groups"},
 "tab_combine": {"pt": "Combinar efeitos", "es": "Combinar efectos", "en": "Combine effects"},
 "tab_soon": {"pt": "Em breve", "es": "Próximamente", "en": "Coming soon"},
 "color_all": {"pt": "Colorir o efeito inteiro...", "es": "Colorear todo el efecto...", "en": "Color whole effect..."},
 "color_marked": {"pt": "Colorir só os marcados...", "es": "Colorear solo los marcados...", "en": "Color checked only..."},
 "color_group": {"pt": "Colorir grupo:", "es": "Colorear grupo:", "en": "Color group:"},
 "pick": {"pt": "Escolher cor...", "es": "Elegir color...", "en": "Pick color..."},
 "keep_sat": {"pt": "Manter saturação original (troca só o tom)", "es": "Mantener saturación original (solo cambia el tono)", "en": "Keep original saturation (hue only)"},
 "manual_rgb": {"pt": "RGB manual do mini-efeito selecionado", "es": "RGB manual del mini efecto seleccionado", "en": "Manual RGB of selected mini-effect"},
 "apply": {"pt": "Aplicar", "es": "Aplicar", "en": "Apply"},
 "select_one": {"pt": "Selecione um mini-efeito na lista.", "es": "Selecciona un mini efecto en la lista.", "en": "Select a mini-effect in the list."},
 "no_colors": {"pt": "Este mini-efeito não tem cores editáveis.", "es": "Este mini efecto no tiene colores editables.", "en": "This mini-effect has no editable colors."},
 "row": {"pt": "Linha", "es": "Fila", "en": "Row"},
 "params_of": {"pt": "Parâmetros do mini-efeito selecionado", "es": "Parámetros del mini efecto seleccionado", "en": "Selected mini-effect parameters"},
 "scale_marked": {"pt": "Escalar tamanho dos marcados ×", "es": "Escalar tamaño de los marcados ×", "en": "Scale size of checked ×"},
 "p_dbt": {"pt": "DBT", "es": "DBT", "en": "DBT"},
 "p_tex": {"pt": "Textura", "es": "Textura", "en": "Texture"},
 "p_delay_a": {"pt": "Atraso A", "es": "Retraso A", "en": "Delay A"},
 "p_delay_b": {"pt": "Atraso B", "es": "Retraso B", "en": "Delay B"},
 "p_dur_a": {"pt": "Duração A", "es": "Duración A", "en": "Duration A"},
 "p_dur_b": {"pt": "Duração B", "es": "Duración B", "en": "Duration B"},
 "p_invoke": {"pt": "Invocação", "es": "Invocación", "en": "Invoke"},
 "p_pos_x": {"pt": "Posição X", "es": "Posición X", "en": "Position X"},
 "p_pos_y": {"pt": "Posição Y (?)", "es": "Posición Y (?)", "en": "Position Y (?)"},
 "p_pos_z": {"pt": "Posição Z (?)", "es": "Posición Z (?)", "en": "Position Z (?)"},
 "p_size1": {"pt": "Tamanho 1", "es": "Tamaño 1", "en": "Size 1"},
 "p_size2": {"pt": "Tamanho 2", "es": "Tamaño 2", "en": "Size 2"},
 "p_size3": {"pt": "Tamanho 3", "es": "Tamaño 3", "en": "Size 3"},
 "p_time1": {"pt": "Tempo 1→2", "es": "Tiempo 1→2", "en": "Time 1→2"},
 "p_time2": {"pt": "Tempo 2→3", "es": "Tiempo 2→3", "en": "Time 2→3"},
 "p_unk30": {"pt": "Desconhecido +0x30", "es": "Desconocido +0x30", "en": "Unknown +0x30"},
 "set_group": {"pt": "Definir grupo dos marcados:", "es": "Asignar grupo a los marcados:", "en": "Set group of checked:"},
 "groups_hint": {"pt": "O jogo não diz o que é aura ou feixe. Os grupos começam separados pela 'invocação' (momento da animação) e você renomeia. Eles ficam salvos num arquivo .grupos.json ao lado do .pak.",
                 "es": "El juego no dice qué es aura o rayo. Los grupos empiezan separados por la 'invocación' (momento de la animación) y tú los renombras. Se guardan en un archivo .grupos.json junto al .pak.",
                 "en": "The game doesn't say what is aura or beam. Groups start split by 'invoke' (animation moment) and you rename them. They are saved in a .grupos.json file next to the .pak."},
 "src_open": {"pt": "Abrir efeito de origem...", "es": "Abrir efecto de origen...", "en": "Open source effect..."},
 "import_marked": {"pt": "Importar marcados da origem", "es": "Importar marcados del origen", "en": "Import checked from source"},
 "replace_group": {"pt": "Antes, remover do efeito atual o grupo:", "es": "Antes, quitar del efecto actual el grupo:", "en": "First remove from current effect the group:"},
 "none": {"pt": "(nenhum)", "es": "(ninguno)", "en": "(none)"},
 "combine_hint": {"pt": "Ex.: abra o efeito da aura, marque o grupo Aura e importe; depois abra o do carregamento e repita; depois o do feixe. Os DBTs vêm junto e os índices são corrigidos sozinhos.",
                  "es": "Ej.: abre el efecto del aura, marca el grupo Aura e importa; luego abre el de la carga y repite; luego el del rayo. Los DBT vienen junto y los índices se corrigen solos.",
                  "en": "E.g.: open the aura effect, check the Aura group and import; then the charge effect; then the beam effect. DBTs come along and indices are fixed automatically."},
 "imported": {"pt": "{n} mini-efeitos importados.", "es": "{n} mini efectos importados.", "en": "{n} mini-effects imported."},
 "soon_text": {"pt": "Ainda não disponível — faltam informações do formato:\n\n• Trocar textura (DBT): precisamos da estrutura do DBT (ou do código do Sparking Studio) para converter PNG → resolução/paleta originais.\n\n• Cena ao acertar + altura: parece envolver o arquivo 02 (só o Pai e Filho tem conteúdo) e parâmetros do personagem fora do eff.\n\n• Tipo de ataque (barragem, feixe, vertical...): o comportamento do golpe fica nos parâmetros do personagem; o eff só muda o visual. Por enquanto use o menu Modelos como base visual.",
               "es": "Aún no disponible — falta información del formato:\n\n• Cambiar textura (DBT): necesitamos la estructura del DBT (o el código de Sparking Studio) para convertir PNG → resolución/paleta originales.\n\n• Escena al acertar + altura: parece involucrar el archivo 02 (solo Padre e Hijo tiene contenido) y parámetros del personaje fuera del eff.\n\n• Tipo de ataque (barrera, rayo, vertical...): el comportamiento del ataque está en los parámetros del personaje; el eff solo cambia lo visual. Por ahora usa el menú Modelos como base visual.",
               "en": "Not available yet — format info missing:\n\n• Texture swap (DBT): we need the DBT structure (or Sparking Studio's code) to convert PNG → original resolution/palette.\n\n• Scene on hit + height: seems to involve file 02 (only Father-Son has content) and character parameters outside the eff.\n\n• Attack type (barrage, beam, vertical...): move behavior lives in character parameters; the eff only changes visuals. For now use the Templates menu as a visual base."},
 "err": {"pt": "Erro", "es": "Error", "en": "Error"},
 "ok": {"pt": "Pronto", "es": "Listo", "en": "Done"},
 "saved": {"pt": "Salvo e validado. Backup: {b}", "es": "Guardado y validado. Copia: {b}", "en": "Saved and validated. Backup: {b}"},
 "saved_nb": {"pt": "Salvo e validado.", "es": "Guardado y validado.", "en": "Saved and validated."},
 "invalid": {"pt": "O efeito ficou inválido, não foi salvo:\n", "es": "El efecto quedó inválido, no se guardó:\n", "en": "Effect became invalid, not saved:\n"},
 "confirm_remove": {"pt": "Remover {n} mini-efeitos marcados?", "es": "¿Eliminar {n} mini efectos marcados?", "en": "Remove {n} checked mini-effects?"},
 "protected": {"pt": "Mini-efeitos do tipo 00 são protegidos e não foram removidos.", "es": "Los mini efectos tipo 00 están protegidos y no se eliminaron.", "en": "Type 00 mini-effects are protected and were not removed."},
 "nothing_marked": {"pt": "Nada marcado.", "es": "Nada marcado.", "en": "Nothing checked."},
 "unsaved": {"pt": "Há alterações não salvas. Sair mesmo assim?", "es": "Hay cambios sin guardar. ¿Salir igualmente?", "en": "There are unsaved changes. Quit anyway?"},
 "source": {"pt": "Origem", "es": "Origen", "en": "Source"},
 "g_aura": {"pt": "Aura", "es": "Aura", "en": "Aura"},
 "g_charge": {"pt": "Carregamento", "es": "Carga", "en": "Charge"},
 "g_projectile": {"pt": "Projétil", "es": "Proyectil", "en": "Projectile"},
 "g_beam": {"pt": "Feixe", "es": "Rayo", "en": "Beam"},
 "g_impact": {"pt": "Impacto/Acerto", "es": "Impacto/Golpe", "en": "Impact/Hit"},
 "g_other": {"pt": "Outro", "es": "Otro", "en": "Other"},
 "g_phase": {"pt": "Fase {n}", "es": "Fase {n}", "en": "Phase {n}"},
}

PRESET_GROUPS = ["aura", "charge", "projectile", "beam", "impact", "explosion", "other"]


def tr(key, lang, **kw):
    s = T.get(key, {}).get(lang) or T.get(key, {}).get("en") or key
    return s.format(**kw) if kw else s


def group_label(g, lang):
    if g in PRESET_GROUPS:
        return tr("g_" + g, lang)
    if g.startswith("phase") and g[5:].isdigit():
        return tr("g_phase", lang, n=g[5:])
    return g

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.2\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.2\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.2\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "more_info": {"pt": "ⓘ Mais informações", "es": "ⓘ Más información", "en": "ⓘ More info"},
 "info_title": {"pt": "Informações", "es": "Información", "en": "Information"},
 "close": {"pt": "Fechar", "es": "Cerrar", "en": "Close"},
 "tex_color": {"pt": "Colorir também as texturas (DBT) ao colorir o efeito inteiro", "es": "Colorear también las texturas (DBT) al colorear todo el efecto", "en": "Also color textures (DBT) when coloring the whole effect"},
 "tex_done": {"pt": "{n} arquivos de textura recoloridos.", "es": "{n} archivos de textura recoloreados.", "en": "{n} texture files recolored."},
 "info_colors": {
  "pt": "COMO A COR FUNCIONA\n\nA cor final de um mini-efeito vem de duas coisas:\n\n1. O SHADER (ou o V00): tabela de cores RGBA que o jogo aplica por cima da textura. É o que o 'RGB manual' edita.\n2. A TEXTURA (DBT): imagens com paleta de 16 ou 256 cores.\n\nQuando você escolhe uma cor, o programa troca o TOM (matiz) de cada cor e mantém o brilho, então partes claras continuam claras e o núcleo branco continua branco.\n\n'Colorir o efeito inteiro' muda shaders, V00 e, se a opção estiver marcada, as paletas de todas as texturas. Só a paleta é alterada; o desenho da textura fica intacto.\n\nTexturas em tons de cinza continuam cinza de propósito: nelas quem dá a cor é o shader.\n\n'Manter saturação original' troca só o tom. Desmarcado, a intensidade da cor escolhida também é aplicada (escolher um cinza deixa o efeito sem cor).\n\nColorir por grupo ou só os marcados não mexe nas texturas, porque uma mesma textura pode ser usada por partes de grupos diferentes.",
  "es": "CÓMO FUNCIONA EL COLOR\n\nEl color final de un mini efecto viene de dos cosas:\n\n1. El SHADER (o el V00): tabla de colores RGBA que el juego aplica encima de la textura. Es lo que edita el 'RGB manual'.\n2. La TEXTURA (DBT): imágenes con paleta de 16 o 256 colores.\n\nAl elegir un color, el programa cambia el TONO de cada color y mantiene el brillo, así las partes claras siguen claras y el núcleo blanco sigue blanco.\n\n'Colorear todo el efecto' cambia shaders, V00 y, si la opción está marcada, las paletas de todas las texturas. Solo se modifica la paleta; el dibujo de la textura queda intacto.\n\nLas texturas en escala de grises siguen grises a propósito: en ellas el color lo da el shader.\n\n'Mantener saturación original' cambia solo el tono. Desmarcado, también se aplica la intensidad del color elegido (elegir un gris deja el efecto sin color).\n\nColorear por grupo o solo los marcados no toca las texturas, porque una misma textura puede ser usada por partes de grupos distintos.",
  "en": "HOW COLOR WORKS\n\nA mini-effect's final color comes from two things:\n\n1. The SHADER (or V00): an RGBA color table the game applies over the texture. This is what 'Manual RGB' edits.\n2. The TEXTURE (DBT): images with a 16 or 256 color palette.\n\nWhen you pick a color, the program swaps the HUE of each color and keeps its brightness, so bright parts stay bright and the white core stays white.\n\n'Color whole effect' changes shaders, V00 and, if the option is checked, the palettes of all textures. Only the palette changes; the texture drawing stays intact.\n\nGrayscale textures stay gray on purpose: the shader gives them color.\n\n'Keep original saturation' swaps only the hue. Unchecked, the chosen color's intensity is applied too (picking a gray removes color).\n\nColoring by group or checked only doesn't touch textures, since one texture can be shared by parts of different groups."},
 "sec_when": {"pt": "Quando aparece", "es": "Cuándo aparece", "en": "When it appears"},
 "sec_dur": {"pt": "Quanto tempo fica", "es": "Cuánto tiempo queda", "en": "How long it stays"},
 "sec_where": {"pt": "Onde aparece", "es": "Dónde aparece", "en": "Where it appears"},
 "sec_size": {"pt": "Tamanho e crescimento", "es": "Tamaño y crecimiento", "en": "Size and growth"},
 "sec_tex": {"pt": "Qual textura usa", "es": "Qué textura usa", "en": "Which texture it uses"},
 "sec_unk": {"pt": "Desconhecido (não mexer)", "es": "Desconocido (no tocar)", "en": "Unknown (don't touch)"},
 "type00_note": {"pt": "Mini-efeito tipo 00: não tem arquivos e seu bloco é diferente dos outros. Nos modelos ele às vezes é o responsável pelo acerto (no Ataque Horizontal do Nappa ele tem invocação 05). Mostrando só os campos seguros.",
                 "es": "Mini efecto tipo 00: no tiene archivos y su bloque es distinto. En los modelos a veces es el responsable del golpe (en el Ataque Horizontal de Nappa tiene invocación 05). Solo se muestran los campos seguros.",
                 "en": "Type 00 mini-effect: has no files and its block differs from the others. In the templates it is sometimes what carries the hit (invoke 05 in Nappa's Horizontal Attack). Showing only safe fields."},
 "h_dbt": {"pt": "Qual arquivo de textura (DBT) da categoria este mini-efeito usa.\n0 = primeiro DBT da categoria, 1 = segundo, e assim por diante.\nSó troque para um número que exista na categoria.",
           "es": "Qué archivo de textura (DBT) de la categoría usa este mini efecto.\n0 = primer DBT de la categoría, 1 = segundo, etc.\nSolo cambia a un número que exista en la categoría.",
           "en": "Which texture file (DBT) of the category this mini-effect uses.\n0 = first DBT of the category, 1 = second, and so on.\nOnly use a number that exists in the category."},
 "h_tex": {"pt": "Qual imagem dentro desse DBT.\n0 = primeira imagem da lista (como aparece no Sparking Studio), 1 = segunda...",
           "es": "Qué imagen dentro de ese DBT.\n0 = primera imagen de la lista (como aparece en Sparking Studio), 1 = segunda...",
           "en": "Which image inside that DBT.\n0 = first image in the list (as shown in Sparking Studio), 1 = second..."},
 "h_delay": {"pt": "Atraso A e Atraso B controlam QUANDO o mini-efeito aparece depois de ser invocado.\nSegundo a documentação, um deles atrasa e o outro adianta, mas ainda não confirmamos qual é qual.\nDica: mude só um por vez, com valores pequenos (1 a 10), e teste no jogo.",
             "es": "Retraso A y Retraso B controlan CUÁNDO aparece el mini efecto después de ser invocado.\nSegún la documentación, uno retrasa y el otro adelanta, pero aún no confirmamos cuál es cuál.\nConsejo: cambia uno a la vez, con valores pequeños (1 a 10), y prueba en el juego.",
             "en": "Delay A and Delay B control WHEN the mini-effect appears after being invoked.\nPer the docs, one delays and the other speeds up, but we haven't confirmed which is which.\nTip: change one at a time, small values (1 to 10), and test in game."},
 "h_dur": {"pt": "Duração A e Duração B aumentam quanto tempo o mini-efeito continua na tela DEPOIS que a animação do golpe termina.\n0 = some junto com a animação.\nAinda não sabemos a diferença exata entre A e B.",
           "es": "Duración A y Duración B aumentan cuánto tiempo sigue el mini efecto en pantalla DESPUÉS de que termina la animación.\n0 = desaparece con la animación.\nAún no sabemos la diferencia exacta entre A y B.",
           "en": "Duration A and B increase how long the mini-effect stays on screen AFTER the move's animation ends.\n0 = disappears with the animation.\nWe don't know the exact difference between A and B yet."},
 "h_pos": {"pt": "Posição do mini-efeito (números com casas decimais).\nPosição X está confirmada pela documentação.\nY e Z são hipóteses (talvez altura e profundidade). Se testar, conte o que aconteceu!",
           "es": "Posición del mini efecto (números con decimales).\nPosición X está confirmada por la documentación.\nY y Z son hipótesis (quizás altura y profundidad). Si pruebas, ¡cuenta qué pasó!",
           "en": "Mini-effect position (decimal numbers).\nPosition X is confirmed by the docs.\nY and Z are hypotheses (maybe height and depth). If you test them, tell us what happened!"},
 "h_size": {"pt": "Um mini-efeito pode ter até 3 tamanhos.\n\n• Só Tamanho 1 preenchido (2 e 3 = 0): o efeito fica sempre desse tamanho.\n• Tamanho 2 preenchido: o efeito cresce/encolhe do Tamanho 1 até o Tamanho 2, levando o 'Tempo 1→2'.\n• Tamanho 3 preenchido: depois ele vai do 2 até o 3, levando o 'Tempo 2→3'.\n\nExemplo: Tamanho 1 = 0, Tamanho 2 = 5, Tempo 1→2 = 0.5 → o efeito nasce do nada e cresce até 5.\n\nO botão 'Escalar tamanho dos marcados' multiplica os três tamanhos de uma vez (1.5 = 50% maior, 0.5 = metade).",
            "es": "Un mini efecto puede tener hasta 3 tamaños.\n\n• Solo Tamaño 1 (2 y 3 = 0): el efecto siempre tiene ese tamaño.\n• Con Tamaño 2: crece/encoge del Tamaño 1 al 2, tardando el 'Tiempo 1→2'.\n• Con Tamaño 3: luego va del 2 al 3, tardando el 'Tiempo 2→3'.\n\nEjemplo: Tamaño 1 = 0, Tamaño 2 = 5, Tiempo 1→2 = 0.5 → el efecto nace de la nada y crece hasta 5.\n\nEl botón 'Escalar tamaño de los marcados' multiplica los tres tamaños a la vez (1.5 = 50% más grande, 0.5 = mitad).",
            "en": "A mini-effect can have up to 3 sizes.\n\n• Only Size 1 set (2 and 3 = 0): the effect always has that size.\n• Size 2 set: it grows/shrinks from Size 1 to Size 2 over 'Time 1→2'.\n• Size 3 set: then it goes from 2 to 3 over 'Time 2→3'.\n\nExample: Size 1 = 0, Size 2 = 5, Time 1→2 = 0.5 → the effect starts from nothing and grows to 5.\n\n'Scale size of checked' multiplies all three sizes at once (1.5 = 50% bigger, 0.5 = half)."},
 "h_invoke": {"pt": "A invocação diz EM QUE MOMENTO da animação do personagem o mini-efeito é chamado. Veja a explicação completa em 'O que são as fases?' na aba Combinar efeitos.\n\n0 → bit 00000010 da animação\n1 → bit 00000100\n2 → sempre no fim da animação (não confirmado)\n3 → bit 00010000\n4 → bit 00100000 · vai no oponente e causa dano\n5 → bit 01000000 · vai no oponente e causa dano",
              "es": "La invocación dice EN QUÉ MOMENTO de la animación del personaje se llama el mini efecto. Mira la explicación completa en '¿Qué son las fases?' en la pestaña Combinar efectos.\n\n0 → bit 00000010 de la animación\n1 → bit 00000100\n2 → siempre al final de la animación (no confirmado)\n3 → bit 00010000\n4 → bit 00100000 · va al oponente y hace daño\n5 → bit 01000000 · va al oponente y hace daño",
              "en": "Invoke says AT WHICH MOMENT of the character's animation the mini-effect is called. See the full explanation in 'What are phases?' in the Combine tab.\n\n0 → animation bit 00000010\n1 → bit 00000100\n2 → always at the end of the animation (unconfirmed)\n3 → bit 00010000\n4 → bit 00100000 · goes to the opponent and deals damage\n5 → bit 01000000 · goes to the opponent and deals damage"},
 "h_unk": {"pt": "Campo cuja função ainda não descobrimos (em um arquivo valia 0.08). Deixe como está, a menos que esteja testando de propósito.",
           "es": "Campo cuya función aún no descubrimos (en un archivo valía 0.08). Déjalo como está, salvo que estés probando a propósito.",
           "en": "Field whose purpose we haven't found yet (0.08 in one file). Leave it unless you're testing on purpose."},
 "what_phases": {"pt": "ⓘ O que são as fases?", "es": "ⓘ ¿Qué son las fases?", "en": "ⓘ What are phases?"},
 "info_phases": {
  "pt": "O QUE SÃO AS FASES\n\nO jogo não guarda 'isto é aura' ou 'isto é feixe'. O que cada mini-efeito tem é um valor de INVOCAÇÃO, que diz em que momento da animação do personagem ele aparece. O programa usa esse valor para montar os grupos iniciais: 'Fase 1' = mini-efeitos com invocação 01, e assim por diante.\n\nDurante o golpe, a animação do personagem vai ligando bits no byte 2 dos parâmetros de animação. Quando um bit liga, os mini-efeitos da fase correspondente aparecem:\n\n• Fase 0 → bit 00000010\n• Fase 1 → bit 00000100\n• Fase 2 → no fim da animação (não confirmado)\n• Fase 3 → bit 00010000\n• Fase 4 → bit 00100000 · lançado no oponente, causa dano\n• Fase 5 → bit 01000000 · lançado no oponente, causa dano\n(as fases 4 e 5 aparecem como 'Impacto/Acerto' e em vermelho)\n\nOu seja, a fase diz QUANDO, não O QUÊ. Em muitos golpes a aura e o carregamento estão nas primeiras fases e o feixe/impacto nas últimas, mas isso varia. O jeito seguro é testar no jogo e renomear os grupos na aba Grupos.\n\nIMPORTANTE AO COMBINAR: o mini-efeito importado continua na fase dele. Se a animação do personagem de destino não liga aquele bit, ele NUNCA aparece. Por isso existe a opção 'Fase dos importados', que troca a fase ao importar (por exemplo, trazer uma aura da Fase 3 para a Fase 1).",
  "es": "QUÉ SON LAS FASES\n\nEl juego no guarda 'esto es aura' o 'esto es rayo'. Lo que tiene cada mini efecto es un valor de INVOCACIÓN, que dice en qué momento de la animación del personaje aparece. El programa usa ese valor para armar los grupos iniciales: 'Fase 1' = mini efectos con invocación 01, etc.\n\nDurante el ataque, la animación del personaje va encendiendo bits en el byte 2 de los parámetros de animación. Cuando se enciende un bit, aparecen los mini efectos de esa fase:\n\n• Fase 0 → bit 00000010\n• Fase 1 → bit 00000100\n• Fase 2 → al final de la animación (no confirmado)\n• Fase 3 → bit 00010000\n• Fase 4 → bit 00100000 · lanzado al oponente, hace daño\n• Fase 5 → bit 01000000 · lanzado al oponente, hace daño\n(las fases 4 y 5 aparecen como 'Impacto/Golpe' y en rojo)\n\nO sea, la fase dice CUÁNDO, no QUÉ. En muchos ataques el aura y la carga están en las primeras fases y el rayo/impacto en las últimas, pero varía. Lo seguro es probar en el juego y renombrar los grupos en la pestaña Grupos.\n\nIMPORTANTE AL COMBINAR: el mini efecto importado sigue en su fase. Si la animación del personaje de destino no enciende ese bit, NUNCA aparece. Por eso existe la opción 'Fase de los importados', que cambia la fase al importar (por ejemplo, traer un aura de la Fase 3 a la Fase 1).",
  "en": "WHAT PHASES ARE\n\nThe game doesn't store 'this is aura' or 'this is beam'. Each mini-effect has an INVOKE value saying at which moment of the character's animation it appears. The program uses it to build the starting groups: 'Phase 1' = mini-effects with invoke 01, etc.\n\nDuring the move, the character's animation turns on bits in byte 2 of the animation parameters. When a bit turns on, that phase's mini-effects appear:\n\n• Phase 0 → bit 00000010\n• Phase 1 → bit 00000100\n• Phase 2 → at the end of the animation (unconfirmed)\n• Phase 3 → bit 00010000\n• Phase 4 → bit 00100000 · thrown at the opponent, deals damage\n• Phase 5 → bit 01000000 · thrown at the opponent, deals damage\n(phases 4 and 5 show as 'Impact/Hit' in red)\n\nSo the phase says WHEN, not WHAT. In many moves the aura and charge are in early phases and the beam/impact in later ones, but it varies. The safe way is to test in game and rename groups in the Groups tab.\n\nIMPORTANT WHEN COMBINING: an imported mini-effect keeps its phase. If the target character's animation never turns that bit on, it NEVER appears. That's why there's the 'Phase of imported' option, which changes the phase on import (e.g. bring an aura from Phase 3 to Phase 1)."},
 "import_phase": {"pt": "Fase dos importados:", "es": "Fase de los importados:", "en": "Phase of imported:"},
 "keep": {"pt": "manter a original", "es": "mantener la original", "en": "keep original"},
 "tab_behavior": {"pt": "Comportamento", "es": "Comportamiento", "en": "Behavior"},
 "beh_model": {"pt": "Modelo de comportamento:", "es": "Modelo de comportamiento:", "en": "Behavior template:"},
 "beh_browse": {"pt": "Outro arquivo...", "es": "Otro archivo...", "en": "Other file..."},
 "beh_apply": {"pt": "Aplicar a parte que acerta do modelo", "es": "Aplicar la parte que golpea del modelo", "en": "Apply the template's hitting part"},
 "beh_current": {"pt": "Efeito atual — partes que acertam:", "es": "Efecto actual — partes que golpean:", "en": "Current effect — hitting parts:"},
 "beh_tpl": {"pt": "Modelo — partes que acertam:", "es": "Modelo — partes que golpean:", "en": "Template — hitting parts:"},
 "beh_none": {"pt": "nenhuma", "es": "ninguna", "en": "none"},
 "beh_bits": {"pt": "A animação do personagem precisa ligar: {b}", "es": "La animación del personaje debe encender: {b}", "en": "Character animation must turn on: {b}"},
 "beh_done": {"pt": "Pronto: {n} mini-efeitos de acerto importados e o tipo 00 copiado do modelo.\nNão esqueça de ajustar o parâmetro do golpe no personagem.", "es": "Listo: {n} mini efectos de golpe importados y el tipo 00 copiado del modelo.\nNo olvides ajustar el parámetro del ataque en el personaje.", "en": "Done: {n} hit mini-effects imported and type 00 copied from the template.\nDon't forget to set the move parameter on the character."},
 "info_behavior": {
  "pt": "COMPORTAMENTO (EXPERIMENTAL)\n\nComo você explicou, o comportamento do golpe tem duas metades:\n\n1. O PARÂMETRO do golpe no personagem: faz a animação e o visual se comportarem como barragem, feixe, ataque de cima etc.\n2. O EFEITO (este .pak): são os mini-efeitos com invocação 04/05 que vão até o oponente e causam o contato/dano. Sem eles, o golpe só 'parece' funcionar.\n\nNos modelos, o mini-efeito tipo 00 (invisível, sem arquivos) também participa: no Ataque Horizontal do Nappa é justamente ele que tem invocação 05. Suspeita: ele funciona como uma área de acerto.\n\nEste botão faz a metade 2:\n• remove as partes que acertam do efeito atual;\n• importa as partes que acertam do modelo (com as texturas);\n• copia o bloco do mini-efeito tipo 00 do modelo.\n\nA metade 1 ainda precisa ser feita à mão no personagem. Se você me passar onde fica esse parâmetro e os valores de cada tipo, o programa pode fazer isso também.\n\nTeste sempre numa cópia do arquivo.",
  "es": "COMPORTAMIENTO (EXPERIMENTAL)\n\nComo explicaste, el comportamiento del ataque tiene dos mitades:\n\n1. El PARÁMETRO del ataque en el personaje: hace que la animación y lo visual se comporten como barrera, rayo, ataque desde arriba, etc.\n2. El EFECTO (este .pak): son los mini efectos con invocación 04/05 que van al oponente y causan el contacto/daño. Sin ellos, el ataque solo 'parece' funcionar.\n\nEn los modelos, el mini efecto tipo 00 (invisible, sin archivos) también participa: en el Ataque Horizontal de Nappa es justamente él quien tiene invocación 05. Sospecha: funciona como área de golpe.\n\nEste botón hace la mitad 2:\n• quita las partes que golpean del efecto actual;\n• importa las partes que golpean del modelo (con texturas);\n• copia el bloque del mini efecto tipo 00 del modelo.\n\nLa mitad 1 todavía hay que hacerla a mano en el personaje. Si me pasas dónde está ese parámetro y los valores de cada tipo, el programa también puede hacerlo.\n\nPrueba siempre en una copia del archivo.",
  "en": "BEHAVIOR (EXPERIMENTAL)\n\nAs you explained, a move's behavior has two halves:\n\n1. The move PARAMETER on the character: makes the animation and visuals act as barrage, beam, attack from above, etc.\n2. The EFFECT (this .pak): the mini-effects with invoke 04/05 that travel to the opponent and cause contact/damage. Without them the move only 'looks' like it works.\n\nIn the templates, the type 00 mini-effect (invisible, no files) takes part too: in Nappa's Horizontal Attack it's the one with invoke 05. Suspicion: it works as a hit area.\n\nThis button does half 2:\n• removes the current effect's hitting parts;\n• imports the template's hitting parts (with textures);\n• copies the template's type 00 block.\n\nHalf 1 still has to be done by hand on the character. If you tell me where that parameter is and each type's values, the program can do it too.\n\nAlways test on a copy of the file."},
 "soon_text": {"pt": "Ainda não disponível:\n\n• Trocar textura por PNG (com conversão de resolução e paleta): a estrutura do DBT já foi decifrada e a troca de cor da paleta já funciona. Falta desembaralhar os pixels (formato PSMT8/PSMT4 do PS2) para importar/exportar imagens.\n\n• Cena ao acertar + altura: parece envolver o arquivo 02 (só o Pai e Filho tem conteúdo) e parâmetros do personagem.\n\n• Parâmetro de comportamento no personagem: aguardando a informação de onde fica.",
               "es": "Aún no disponible:\n\n• Cambiar textura por PNG (con conversión de resolución y paleta): la estructura del DBT ya se descifró y el cambio de color de la paleta ya funciona. Falta desordenar los píxeles (formato PSMT8/PSMT4 de PS2) para importar/exportar imágenes.\n\n• Escena al acertar + altura: parece involucrar el archivo 02 (solo Padre e Hijo tiene contenido) y parámetros del personaje.\n\n• Parámetro de comportamiento en el personaje: esperando la información de dónde está.",
               "en": "Not available yet:\n\n• Replace texture with PNG (with resolution/palette conversion): the DBT structure is decoded and palette recoloring works. Pixel unswizzling (PS2 PSMT8/PSMT4) is still needed to import/export images.\n\n• Scene on hit + height: seems to involve file 02 (only Father-Son has content) and character parameters.\n\n• Behavior parameter on the character: waiting for info on where it lives.",},
 "g_phase_end": {"pt": "Fase 2 (fim)", "es": "Fase 2 (final)", "en": "Phase 2 (end)"},
})


def group_label(g, lang):
    if g in PRESET_GROUPS:
        return tr("g_" + g, lang)
    if g.startswith("extra:"):
        parts = g.split(":")
        return "✚ " + tr("kind_" + parts[1], lang) + " (" + tr("slot_" + parts[2], lang).lower() + ")"
    if g == "phase2":
        return tr("g_phase_end", lang)
    if g.startswith("phase") and g[5:].isdigit():
        return tr("g_phase", lang, n=g[5:])
    return g

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.3\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.3\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.3\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "mark_groups": {"pt": "Marcar grupos:", "es": "Marcar grupos:", "en": "Check groups:"},
 "import_marked": {"pt": "✔ Aplicar combinação (importar os marcados)", "es": "✔ Aplicar combinación (importar los marcados)", "en": "✔ Apply combination (import checked)"},
 "session_row": {"pt": "Sessão {s} · linha {r}", "es": "Sesión {s} · fila {r}", "en": "Session {s} · row {r}"},
})

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.4\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.4\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.4\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "display": {"pt": "Exibição", "es": "Pantalla", "en": "Display"},
 "win_size": {"pt": "Tamanho da janela", "es": "Tamaño de ventana", "en": "Window size"},
 "win_auto": {"pt": "Automático (conforme o monitor)", "es": "Automático (según el monitor)", "en": "Automatic (fit monitor)"},
 "win_max": {"pt": "Maximizada", "es": "Maximizada", "en": "Maximized"},
 "ui_scale": {"pt": "Escala da interface", "es": "Escala de la interfaz", "en": "Interface scale"},
 "panel_pos": {"pt": "Posição do painel de abas", "es": "Posición del panel de pestañas", "en": "Tab panel position"},
 "layout_right": {"pt": "À direita da lista", "es": "A la derecha de la lista", "en": "Right of the list"},
 "layout_bottom": {"pt": "Embaixo da lista (telas estreitas)", "es": "Debajo de la lista (pantallas estrechas)", "en": "Below the list (narrow screens)"},
 "rep_phase": {"pt": "Substituir as mesmas fases no efeito atual (recomendado)", "es": "Sustituir las mismas fases en el efecto actual (recomendado)", "en": "Replace the same phases in the current effect (recommended)"},
 "rep_group": {"pt": "Substituir o grupo:", "es": "Sustituir el grupo:", "en": "Replace group:"},
 "rep_add": {"pt": "Só adicionar (não remove nada — pode duplicar)", "es": "Solo añadir (no quita nada — puede duplicar)", "en": "Add only (removes nothing — may duplicate)"},
 "imported2": {"pt": "{n} mini-efeitos importados, {r} substituídos.", "es": "{n} mini efectos importados, {r} sustituidos.", "en": "{n} mini-effects imported, {r} replaced."},
})

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.5\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.5\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.5\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "scale_group": {"pt": "Escalar grupo/fase inteiro:", "es": "Escalar grupo/fase entero:", "en": "Scale whole group/phase:"},
 "scaled": {"pt": "{n} mini-efeitos redimensionados.", "es": "{n} mini efectos redimensionados.", "en": "{n} mini-effects resized."},
 "tab_scene": {"pt": "Cena ao acertar", "es": "Escena al acertar", "en": "Scene on hit"},
 "scene_current": {"pt": "Atual:", "es": "Actual:", "en": "Current:"},
 "scene_none": {"pt": "Sem cena", "es": "Sin escena", "en": "No scene"},
 "scene_ground": {"pt": "Manter no chão a partir do evento 2 da animação", "es": "Mantener en el suelo desde el evento 2 de la animación", "en": "Keep on the ground from animation event 2"},
 "scene_air": {"pt": "Jogar pro ar a partir do evento 2 da animação", "es": "Lanzar al aire desde el evento 2 de la animación", "en": "Throw into the air from animation event 2"},
 "scene_custom": {"pt": "Cena personalizada (copiada de outro efeito)", "es": "Escena personalizada (copiada de otro efecto)", "en": "Custom scene (copied from another effect)"},
 "scene_missing": {"pt": "(falta o arquivo de referência — veja abaixo)", "es": "(falta el archivo de referencia — ver abajo)", "en": "(reference file missing — see below)"},
 "scene_copy": {"pt": "Copiar a cena de outro .pak...", "es": "Copiar la escena de otro .pak...", "en": "Copy the scene from another .pak..."},
 "scene_save_as": {"pt": "Guardar a cena deste efeito como:", "es": "Guardar la escena de este efecto como:", "en": "Store this effect's scene as:"},
 "scene_empty": {"pt": "Este efeito não tem cena (arquivo 02 vazio).", "es": "Este efecto no tiene escena (archivo 02 vacío).", "en": "This effect has no scene (file 02 empty)."},
 "info_scene": {
  "pt": "CENA AO ACERTAR (EXPERIMENTAL)\n\nOs golpes com cena têm o arquivo 02 do efeito preenchido (2816 bytes). Nos efeitos sem cena ele existe, mas vazio. Ele parece guardar uma tabela de 176 linhas com posições, e a diferença entre 'manter no chão' e 'jogar pro ar' está nela.\n\nOpções:\n• Sem cena: deixa o arquivo 02 vazio.\n• Manter no chão / Jogar pro ar: copia a tabela de um efeito de referência que está na pasta 'cenas'.\n\nComo cadastrar ou corrigir as referências: abra um efeito que você sabe que mantém no chão e clique em 'Guardar a cena deste efeito como: Chão'. Faça o mesmo com um que joga pro ar. Isso vale para os próximos efeitos também.\n\n'Copiar a cena de outro .pak' traz a cena de qualquer efeito, sem precisar cadastrar.\n\nO evento 2 da animação é só para você saber a partir de qual momento a cena influencia: o programa não mexe na animação. Lembre que o golpe também precisa estar configurado no personagem para ter cena.",
  "es": "ESCENA AL ACERTAR (EXPERIMENTAL)\n\nLos ataques con escena tienen el archivo 02 del efecto lleno (2816 bytes). En los efectos sin escena existe, pero vacío. Parece guardar una tabla de 176 filas con posiciones, y la diferencia entre 'mantener en el suelo' y 'lanzar al aire' está en ella.\n\nOpciones:\n• Sin escena: deja el archivo 02 vacío.\n• Mantener en el suelo / Lanzar al aire: copia la tabla de un efecto de referencia de la carpeta 'cenas'.\n\nCómo registrar o corregir las referencias: abre un efecto que sabes que mantiene en el suelo y haz clic en 'Guardar la escena de este efecto como: Suelo'. Haz lo mismo con uno que lanza al aire. Sirve para los próximos efectos también.\n\n'Copiar la escena de otro .pak' trae la escena de cualquier efecto, sin registrarla.\n\nEl evento 2 de la animación es solo para que sepas desde qué momento influye la escena: el programa no toca la animación. Recuerda que el ataque también debe estar configurado en el personaje para tener escena.",
  "en": "SCENE ON HIT (EXPERIMENTAL)\n\nMoves with a scene have the effect's file 02 filled (2816 bytes). In effects without a scene it exists but is empty. It seems to hold a 176-row table of positions, and the difference between 'keep on ground' and 'throw into the air' lives there.\n\nOptions:\n• No scene: leaves file 02 empty.\n• Keep on ground / Throw into air: copies the table from a reference effect in the 'cenas' folder.\n\nHow to register or fix references: open an effect you know keeps on the ground and click 'Store this effect's scene as: Ground'. Do the same with one that throws into the air. It works for future effects too.\n\n'Copy the scene from another .pak' brings any effect's scene without registering it.\n\nAnimation event 2 is only so you know from which moment the scene applies: the program doesn't touch the animation. Remember the move must also be set up on the character to have a scene."},
 "w_btn": {"pt": "Peso...", "es": "Peso...", "en": "Size..."},
 "w_title": {"pt": "De onde vem o peso do efeito", "es": "De dónde viene el peso del efecto", "en": "Where the effect's size comes from"},
 "w_warn": {"pt": "acima de 200 KB", "es": "más de 200 KB", "en": "over 200 KB"},
 "w_total": {"pt": "Tamanho total: {kb:.1f} KB", "es": "Tamaño total: {kb:.1f} KB", "en": "Total size: {kb:.1f} KB"},
 "w_dbt": {"pt": "Texturas (DBT): {kb:.1f} KB — maiores primeiro:", "es": "Texturas (DBT): {kb:.1f} KB — mayores primero:", "en": "Textures (DBT): {kb:.1f} KB — largest first:"},
 "w_other": {"pt": "Shapes, shaders, V00 e animações: {kb:.1f} KB", "es": "Shapes, shaders, V00 y animaciones: {kb:.1f} KB", "en": "Shapes, shaders, V00 and animations: {kb:.1f} KB"},
 "w_pre": {"pt": "Arquivos 00–02 (modelos 3D, cena): {kb:.1f} KB", "es": "Archivos 00–02 (modelos 3D, escena): {kb:.1f} KB", "en": "Files 00–02 (3D models, scene): {kb:.1f} KB"},
 "w_tip": {"pt": "Quase todo o peso vem das texturas. Ao combinar efeitos, as texturas dos dois lados passam a existir no mesmo arquivo, então o tamanho cresce de verdade: não é duplicação. Para aliviar, remova (ou substitua) os grupos que usam os DBTs mais pesados da lista acima. Quando um DBT fica sem uso, ele sai do arquivo sozinho.",
           "es": "Casi todo el peso viene de las texturas. Al combinar efectos, las texturas de ambos lados pasan a estar en el mismo archivo, así que el tamaño crece de verdad: no es duplicación. Para aligerar, quita (o sustituye) los grupos que usan los DBT más pesados de la lista. Cuando un DBT queda sin uso, sale del archivo solo.",
           "en": "Almost all the size comes from textures. When combining effects, both sides' textures end up in the same file, so the size really grows: it's not duplication. To slim it down, remove (or replace) the groups using the heaviest DBTs listed above. When a DBT is no longer used, it leaves the file automatically."},
})

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.6\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.6\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.6\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "hide_marked": {"pt": "Ocultar marcados", "es": "Ocultar marcados", "en": "Hide checked"},
 "phase_tools": {"pt": "Remover ou ocultar uma fase/grupo", "es": "Quitar u ocultar una fase/grupo", "en": "Remove or hide a phase/group"},
 "group_or_phase": {"pt": "Fase/grupo:", "es": "Fase/grupo:", "en": "Phase/group:"},
 "hide_alpha": {"pt": "Invisível por transparência (mantém tamanho — recomendado)", "es": "Invisible por transparencia (mantiene tamaño — recomendado)", "en": "Invisible via transparency (keeps size — recommended)"},
 "hide_size": {"pt": "Invisível por tamanho 0", "es": "Invisible por tamaño 0", "en": "Invisible via size 0"},
 "hide_group": {"pt": "Tornar invisível", "es": "Hacer invisible", "en": "Make invisible"},
 "remove_group": {"pt": "Remover do efeito", "es": "Quitar del efecto", "en": "Remove from effect"},
 "hidden": {"pt": "{n} mini-efeitos ficaram invisíveis.", "es": "{n} mini efectos quedaron invisibles.", "en": "{n} mini-effects are now invisible."},
 "hidden_skip": {"pt": "{n} não têm cor editável (ex.: animação tipo 02) e não mudaram — use 'tamanho 0' neles.", "es": "{n} no tienen color editable (ej.: animación tipo 02) y no cambiaron — usa 'tamaño 0' en ellos.", "en": "{n} have no editable color (e.g. type 02 animation) and didn't change — use 'size 0' on them."},
 "warn_hits": {"pt": "Atenção: entre eles há partes que ACERTAM o oponente (invocação 04/05). Removendo, o golpe pode deixar de causar dano. Para só esconder o visual, use 'Tornar invisível'.",
               "es": "Atención: entre ellos hay partes que GOLPEAN al oponente (invocación 04/05). Si los quitas, el ataque puede dejar de hacer daño. Para solo esconder lo visual, usa 'Hacer invisible'.",
               "en": "Warning: some of them HIT the opponent (invoke 04/05). Removing them may stop the move from dealing damage. To only hide the visuals, use 'Make invisible'."},
 "info_hide": {
  "pt": "REMOVER x TORNAR INVISÍVEL\n\nREMOVER tira os mini-efeitos do arquivo. As texturas (DBT) que só eles usavam também saem, então o arquivo fica mais leve. Cuidado com as partes que acertam (fases 4 e 5, em vermelho): sem elas o golpe pode não causar dano.\n\nTORNAR INVISÍVEL mantém os mini-efeitos no arquivo, com o mesmo momento e a mesma função, mas sem aparecer. Ideal para esconder o visual de uma parte que acerta sem perder o dano. O arquivo não fica mais leve.\n\n• Por transparência (recomendado): zera o canal A das cores do shader/V00. O tamanho continua o mesmo, o que deve preservar a área de acerto.\n• Por tamanho 0: zera os tamanhos 1, 2 e 3. Funciona até em partes sem cor editável, mas pode reduzir a área de acerto.\n\nNenhum dos dois mexe nas texturas, que podem ser usadas por outras partes. Para desfazer, use Ctrl+Z ou importe a fase de novo a partir do arquivo original. (Experimental: confirme no jogo.)",
  "es": "QUITAR vs HACER INVISIBLE\n\nQUITAR saca los mini efectos del archivo. Las texturas (DBT) que solo ellos usaban también salen, así que el archivo queda más liviano. Cuidado con las partes que golpean (fases 4 y 5, en rojo): sin ellas el ataque puede no hacer daño.\n\nHACER INVISIBLE mantiene los mini efectos en el archivo, con el mismo momento y función, pero sin verse. Ideal para esconder lo visual de una parte que golpea sin perder el daño. El archivo no queda más liviano.\n\n• Por transparencia (recomendado): pone en cero el canal A de los colores del shader/V00. El tamaño sigue igual, lo que debería preservar el área de golpe.\n• Por tamaño 0: pone en cero los tamaños 1, 2 y 3. Funciona incluso sin color editable, pero puede reducir el área de golpe.\n\nNinguno toca las texturas, que pueden ser usadas por otras partes. Para deshacer, usa Ctrl+Z o importa la fase de nuevo desde el archivo original. (Experimental: confírmalo en el juego.)",
  "en": "REMOVE vs MAKE INVISIBLE\n\nREMOVE takes the mini-effects out of the file. Textures (DBT) used only by them go too, so the file gets lighter. Careful with hitting parts (phases 4 and 5, in red): without them the move may deal no damage.\n\nMAKE INVISIBLE keeps the mini-effects in the file, same timing and function, but not shown. Ideal to hide a hitting part's visuals without losing damage. The file doesn't get lighter.\n\n• Via transparency (recommended): zeroes the A channel of shader/V00 colors. Size stays, which should preserve the hit area.\n• Via size 0: zeroes sizes 1, 2 and 3. Works even without editable color, but may shrink the hit area.\n\nNeither touches textures, which other parts may share. To undo, use Ctrl+Z or import the phase again from the original file. (Experimental: confirm in game.)"},
})

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.7\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.7\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.7\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "g_explosion": {"pt": "Explosão (Vfx 5)", "es": "Explosión (Vfx 5)", "en": "Explosion (Vfx 5)"},
 "beh_opt_hits": {"pt": "Partes que acertam (fases 4/5) + bloco tipo 00", "es": "Partes que golpean (fases 4/5) + bloque tipo 00", "en": "Hitting parts (phases 4/5) + type 00 block"},
 "beh_opt_launch": {"pt": "Formato do lançamento (fases 1, 2 e 3)", "es": "Forma del lanzamiento (fases 1, 2 y 3)", "en": "Launch shape (phases 1, 2 and 3)"},
 "beh_opt_color": {"pt": "Pintar o que vier com a cor predominante do efeito atual", "es": "Pintar lo que venga con el color predominante del efecto actual", "en": "Paint what comes in with the current effect's dominant color"},
 "beh_done2": {"pt": "Pronto: {n} mini-efeitos vieram do modelo (o carregamento/fase 0 do seu efeito foi mantido).\nNão esqueça de ajustar o parâmetro do golpe no personagem.", "es": "Listo: {n} mini efectos vinieron del modelo (la carga/fase 0 de tu efecto se mantuvo).\nNo olvides ajustar el parámetro del ataque en el personaje.", "en": "Done: {n} mini-effects came from the template (your effect's charge/phase 0 was kept).\nDon't forget to set the move parameter on the character."},
 "painted": {"pt": "Pintados com a cor {c}.", "es": "Pintados con el color {c}.", "en": "Painted with color {c}."},
 "expl_title": {"pt": "Explosão no oponente (evento Vfx 5)", "es": "Explosión en el oponente (evento Vfx 5)", "en": "Explosion on the opponent (Vfx 5 event)"},
 "dominant": {"pt": "Cor predominante do efeito:", "es": "Color predominante del efecto:", "en": "Effect's dominant color:"},
 "expl_color": {"pt": "Pintar a explosão com a cor predominante", "es": "Pintar la explosión con el color predominante", "en": "Paint the explosion with the dominant color"},
 "expl_add": {"pt": "Adicionar explosão", "es": "Añadir explosión", "en": "Add explosion"},
 "expl_done": {"pt": "Explosão adicionada ({n} mini-efeitos na fase 4).\nNa animação do golpe, o evento 'Vfx 5' precisa estar ativo no momento da explosão.", "es": "Explosión añadida ({n} mini efectos en la fase 4).\nEn la animación del ataque, el evento 'Vfx 5' debe estar activo en el momento de la explosión.", "en": "Explosion added ({n} mini-effects in phase 4).\nIn the move's animation, the 'Vfx 5' event must be active at the moment of the explosion."},
 "expl_noscene": {"pt": "Este efeito não tem cena. A explosão foi pensada para golpes com cena. Adicionar mesmo assim?", "es": "Este efecto no tiene escena. La explosión fue pensada para ataques con escena. ¿Añadir de todos modos?", "en": "This effect has no scene. The explosion was made for moves with a scene. Add anyway?"},
 "info_expl": {
  "pt": "EXPLOSÃO (VFX 5)\n\nA explosão azul ao fundo dos golpes com cena são mini-efeitos com invocação 04. Na documentação, invocação 04 = 'VFX 5', o mesmo nome que o plugin de animação do Blender dá ao evento. Ou seja: quando a animação liga o evento Vfx 5, os mini-efeitos da fase 4 aparecem, lançados no oponente.\n\nO botão:\n• remove a fase 4 que o efeito já tiver (para não duplicar);\n• importa os mini-efeitos da explosão (arquivo extras/explosao_vfx5.pak) junto com as texturas;\n• pinta a explosão e as texturas dela com a cor predominante do efeito (mostrada acima).\n\nA cor predominante é a média dos tons do efeito, pesando mais as cores fortes e visíveis.\n\nPara ela aparecer, a animação do golpe precisa ter o evento Vfx 5 no momento certo (isso se faz no Blender). Para trocar a explosão padrão, substitua o arquivo em 'extras' por outro efeito que tenha a fase 4.",
  "es": "EXPLOSIÓN (VFX 5)\n\nLa explosión azul al fondo de los ataques con escena son mini efectos con invocación 04. En la documentación, invocación 04 = 'VFX 5', el mismo nombre que el plugin de animación de Blender da al evento. O sea: cuando la animación enciende el evento Vfx 5, aparecen los mini efectos de la fase 4, lanzados al oponente.\n\nEl botón:\n• quita la fase 4 que ya tenga el efecto (para no duplicar);\n• importa los mini efectos de la explosión (archivo extras/explosao_vfx5.pak) junto con sus texturas;\n• pinta la explosión y sus texturas con el color predominante del efecto (mostrado arriba).\n\nEl color predominante es el promedio de tonos del efecto, dando más peso a los colores fuertes y visibles.\n\nPara que aparezca, la animación del ataque debe tener el evento Vfx 5 en el momento correcto (eso se hace en Blender). Para cambiar la explosión por defecto, sustituye el archivo en 'extras' por otro efecto que tenga fase 4.",
  "en": "EXPLOSION (VFX 5)\n\nThe blue explosion in the background of scene moves is made of mini-effects with invoke 04. In the docs, invoke 04 = 'VFX 5', the same name the Blender animation plugin gives the event. So when the animation turns on the Vfx 5 event, phase 4 mini-effects appear, thrown at the opponent.\n\nThe button:\n• removes any existing phase 4 (to avoid duplicates);\n• imports the explosion mini-effects (extras/explosao_vfx5.pak) with their textures;\n• paints the explosion and its textures with the effect's dominant color (shown above).\n\nThe dominant color is the average hue of the effect, weighting strong visible colors more.\n\nFor it to show, the move's animation needs the Vfx 5 event at the right moment (done in Blender). To change the default explosion, replace the file in 'extras' with another effect that has phase 4."},
 "info_behavior": {
  "pt": "COMPORTAMENTO (EXPERIMENTAL)\n\nO comportamento do golpe tem duas metades:\n1. O PARÂMETRO do golpe no personagem (feito à mão, por enquanto).\n2. O EFEITO: é isso que este botão troca.\n\nO que vem do modelo:\n• Partes que acertam (fases 4/5) e o bloco do mini-efeito tipo 00 — sempre. O tipo 00 parece controlar o projétil/área de acerto (nos modelos, os valores dele mudam entre área, vertical e barragem).\n• Formato do lançamento (fases 1, 2 e 3) — opcional, ligado por padrão. É o 'desenho' do disparo: no Madam, a esfera que vai; no Vertical, o que sobe; na Barragem, os tiros.\n\nO que fica do seu efeito: o carregamento (fase 0).\n\nCom 'Pintar...' ligado, tudo o que veio do modelo (inclusive as texturas usadas só por essas partes) ganha a cor predominante do seu efeito, para não ficar com a cor do modelo.\n\nTeste sempre numa cópia do arquivo.",
  "es": "COMPORTAMIENTO (EXPERIMENTAL)\n\nEl comportamiento del ataque tiene dos mitades:\n1. El PARÁMETRO del ataque en el personaje (a mano, por ahora).\n2. El EFECTO: es lo que cambia este botón.\n\nLo que viene del modelo:\n• Partes que golpean (fases 4/5) y el bloque del mini efecto tipo 00 — siempre. El tipo 00 parece controlar el proyectil/área de golpe (en los modelos, sus valores cambian entre área, vertical y barrera).\n• Forma del lanzamiento (fases 1, 2 y 3) — opcional, activada por defecto. Es el 'dibujo' del disparo: en Madam, la esfera que va; en Vertical, lo que sube; en Barrera, los disparos.\n\nLo que queda de tu efecto: la carga (fase 0).\n\nCon 'Pintar...' activado, todo lo que vino del modelo (incluidas las texturas usadas solo por esas partes) recibe el color predominante de tu efecto.\n\nPrueba siempre en una copia del archivo.",
  "en": "BEHAVIOR (EXPERIMENTAL)\n\nA move's behavior has two halves:\n1. The move PARAMETER on the character (by hand, for now).\n2. The EFFECT: this is what the button swaps.\n\nWhat comes from the template:\n• Hitting parts (phases 4/5) and the type 00 block — always. Type 00 seems to control the projectile/hit area (its values change between area, vertical and barrage templates).\n• Launch shape (phases 1, 2 and 3) — optional, on by default. It's the 'drawing' of the shot: in Madam, the sphere that flies; in Vertical, what goes up; in Barrage, the shots.\n\nWhat stays from your effect: the charge (phase 0).\n\nWith 'Paint...' on, everything from the template (including textures used only by those parts) gets your effect's dominant color.\n\nAlways test on a copy of the file."},
})

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.8\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.8\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.8\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "tab_extras": {"pt": "Extras", "es": "Extras", "en": "Extras"},
 "extras_hint": {"pt": "Mini-efeitos complementares: só enfeitam, não mudam o formato nem a classe do golpe. Marque ou desmarque e clique em Aplicar.", "es": "Mini efectos complementarios: solo decoran, no cambian la forma ni la clase del ataque. Marca o desmarca y haz clic en Aplicar.", "en": "Complementary mini-effects: decoration only, they don't change the move's shape or class. Check or uncheck and click Apply."},
 "slot_charge": {"pt": "Antes do disparo", "es": "Antes del disparo", "en": "Before the shot"},
 "slot_launch": {"pt": "Disparo", "es": "Disparo", "en": "Shot"},
 "kind_swirl": {"pt": "Redemoinho", "es": "Remolino", "en": "Swirl"},
 "kind_orbs": {"pt": "Bolinhas", "es": "Bolitas", "en": "Orbs"},
 "kind_x": {"pt": "Extra", "es": "Extra", "en": "Extra"},
 "extras_apply": {"pt": "Aplicar extras", "es": "Aplicar extras", "en": "Apply extras"},
 "extras_done": {"pt": "{a} mini-efeitos adicionados, {r} removidos.\n(Disparo deste efeito: fase {p})", "es": "{a} mini efectos añadidos, {r} quitados.\n(Disparo de este efecto: fase {p})", "en": "{a} mini-effects added, {r} removed.\n(This effect's shot: phase {p})"},
 "expl_color": {"pt": "Pintar com a cor predominante do efeito", "es": "Pintar con el color predominante del efecto", "en": "Paint with the effect's dominant color"},
 "info_extras": {
  "pt": "EXTRAS\n\nSão enfeites que você liga e desliga sem mexer no formato do golpe:\n\n• Antes do disparo: entram na fase 0 (carregamento).\n• Disparo: entram na fase do disparo do efeito, detectada pelo mini-efeito tipo 00 (fase 1 no Madam, fase 3 na Barragem e no Vertical).\n\nCom 'Pintar...' ligado, o extra e as texturas dele ganham a cor predominante do efeito.\n\nDesmarcar e aplicar remove o extra (e as texturas que só ele usava). O programa reconhece os extras pelo grupo, que fica salvo no arquivo .grupos.json ao lado do .pak.\n\nPara criar novos extras: coloque um .pak com os mini-efeitos na pasta 'extras' e registre no extras.json (arquivo, slot 'charge' ou 'launch', e tipo).",
  "es": "EXTRAS\n\nSon adornos que activas y desactivas sin tocar la forma del ataque:\n\n• Antes del disparo: entran en la fase 0 (carga).\n• Disparo: entran en la fase del disparo del efecto, detectada por el mini efecto tipo 00 (fase 1 en Madam, fase 3 en Barrera y Vertical).\n\nCon 'Pintar...' activado, el extra y sus texturas reciben el color predominante del efecto.\n\nDesmarcar y aplicar quita el extra (y las texturas que solo él usaba). El programa reconoce los extras por el grupo, que se guarda en el archivo .grupos.json junto al .pak.\n\nPara crear nuevos extras: pon un .pak con los mini efectos en la carpeta 'extras' y regístralo en extras.json (archivo, slot 'charge' o 'launch', y tipo).",
  "en": "EXTRAS\n\nDecorations you turn on and off without touching the move's shape:\n\n• Before the shot: go into phase 0 (charge).\n• Shot: go into the effect's shot phase, detected from the type 00 mini-effect (phase 1 in Madam, phase 3 in Barrage and Vertical).\n\nWith 'Paint...' on, the extra and its textures get the effect's dominant color.\n\nUnchecking and applying removes the extra (and textures only it used). Extras are recognized by group, saved in the .grupos.json next to the .pak.\n\nTo create new extras: put a .pak with the mini-effects in the 'extras' folder and register it in extras.json (file, slot 'charge' or 'launch', and kind)."},
})

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.9\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.9\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.9\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "beh_opt_header": {"pt": "Parâmetros de lançamento do cabeçalho (direção vertical, alcance)", "es": "Parámetros de lanzamiento del encabezado (dirección vertical, alcance)", "en": "Header launch parameters (vertical direction, range)"},
 "nerf_title": {"pt": "Reduzir cores das texturas (256 → 16)", "es": "Reducir colores de las texturas (256 → 16)", "en": "Reduce texture colors (256 → 16)"},
 "nerf_all": {"pt": "Todas as texturas", "es": "Todas las texturas", "en": "All textures"},
 "nerf_marked": {"pt": "Só as dos marcados", "es": "Solo las de los marcados", "en": "Only checked ones'"},
 "depth": {"pt": "Imagens com 256 cores: {a} · com 16 cores: {b}", "es": "Imágenes con 256 colores: {a} · con 16 colores: {b}", "en": "Images with 256 colors: {a} · with 16 colors: {b}"},
 "nerf_done": {"pt": "{n} imagens reduzidas para 16 cores.\nTamanho: {b:.0f} KB → {a:.0f} KB", "es": "{n} imágenes reducidas a 16 colores.\nTamaño: {b:.0f} KB → {a:.0f} KB", "en": "{n} images reduced to 16 colors.\nSize: {b:.0f} KB → {a:.0f} KB"},
 "info_nerf": {
  "pt": "REDUZIR CORES\n\nO programa nunca muda a quantidade de cores sozinho: colorir, combinar e os extras mantêm cada textura no formato original (256 ou 16 cores). O peso a mais nos efeitos combinados vem das texturas dos dois efeitos somadas.\n\nEste botão converte texturas de 256 cores (8 bits por pixel) para 16 cores (4 bits por pixel), o mesmo formato que o jogo já usa em várias texturas. O desenho de cada textura cai pela metade e a paleta cai de 1 KB para 64 bytes. No Madam, por exemplo, o arquivo vai de 153 KB para 86 KB.\n\nA redução escolhe as 16 cores que melhor representam cada imagem. Brilhos e degradês podem ganhar um pouco de 'degrau'; teste no jogo. Texturas que já têm 16 cores ou menos não mudam. Ctrl+Z desfaz.",
  "es": "REDUCIR COLORES\n\nEl programa nunca cambia la cantidad de colores por su cuenta: colorear, combinar y los extras mantienen cada textura en su formato original (256 o 16 colores). El peso extra de los efectos combinados viene de sumar las texturas de ambos efectos.\n\nEste botón convierte texturas de 256 colores (8 bits por píxel) a 16 colores (4 bits por píxel), el mismo formato que el juego ya usa en varias texturas. El dibujo de cada textura se reduce a la mitad y la paleta pasa de 1 KB a 64 bytes. En Madam, por ejemplo, el archivo pasa de 153 KB a 86 KB.\n\nLa reducción elige los 16 colores que mejor representan cada imagen. Brillos y degradados pueden quedar un poco 'escalonados'; prueba en el juego. Las texturas que ya tienen 16 colores o menos no cambian. Ctrl+Z deshace.",
  "en": "REDUCE COLORS\n\nThe program never changes color count on its own: coloring, combining and extras keep each texture in its original format (256 or 16 colors). The extra size in combined effects comes from both effects' textures added together.\n\nThis button converts 256-color textures (8 bits per pixel) to 16 colors (4 bits per pixel), a format the game already uses for many textures. Each texture's pixel data halves and the palette drops from 1 KB to 64 bytes. Madam, for example, goes from 153 KB to 86 KB.\n\nThe reduction picks the 16 colors that best represent each image. Glows and gradients may get slight banding; test in game. Textures already at 16 colors or fewer don't change. Ctrl+Z undoes."},
})

T.update({
 "about_text": {"pt": "BT3 Effect Studio v0.10\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
                "es": "BT3 Effect Studio v0.10\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
                "en": "BT3 Effect Studio v0.10\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."},
 "slot_pair": {"pt": "Carregamento + disparo", "es": "Carga + disparo", "en": "Charge + shot"},
 "beh_mode_shape": {"pt": "Comportamento + formato do modelo", "es": "Comportamiento + forma del modelo", "en": "Behavior + template shape"},
 "beh_mode_only": {"pt": "Só comportamento (mantém o formato do seu efeito)", "es": "Solo comportamiento (mantiene la forma de tu efecto)", "en": "Behavior only (keeps your effect's shape)"},
 "beh_done_only": {"pt": "Pronto: o formato do seu efeito foi mantido.\n{n} mini-efeitos do disparo foram ajustados para o disparo do modelo (fase {p}), e o cabeçalho e o tipo 00 vieram do modelo.\nNão esqueça de ajustar o parâmetro do golpe no personagem.", "es": "Listo: la forma de tu efecto se mantuvo.\n{n} mini efectos del disparo se ajustaron al disparo del modelo (fase {p}); el encabezado y el tipo 00 vinieron del modelo.\nNo olvides ajustar el parámetro del ataque en el personaje.", "en": "Done: your effect's shape was kept.\n{n} shot mini-effects were adjusted to the template's shot (phase {p}); header and type 00 came from the template.\nDon't forget to set the move parameter on the character."},
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.11\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.11\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.11\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "slot_aura": {
  "pt": "Aura antes do disparo",
  "es": "Aura antes del disparo",
  "en": "Aura before the shot"
 },
 "kind_lightning": {
  "pt": "Raios (Makankosappo)",
  "es": "Rayos (Makankosappo)",
  "en": "Lightning (Makankosappo)"
 },
 "kind_rings": {
  "pt": "Argolas (Makankosappo)",
  "es": "Anillos (Makankosappo)",
  "en": "Rings (Makankosappo)"
 },
 "kind_lightbeams": {
  "pt": "Feixes luminosos (Kamehameha)",
  "es": "Haces luminosos (Kamehameha)",
  "en": "Light beams (Kamehameha)"
 },
 "kind_strong_lightning": {
  "pt": "Raios intensos (Shin/Raditz)",
  "es": "Rayos intensos (Shin/Raditz)",
  "en": "Intense lightning (Shin/Raditz)"
 },
 "kind_circle_swirl": {
  "pt": "Redemoinho circular (Shin)",
  "es": "Remolino circular (Shin)",
  "en": "Circular swirl (Shin)"
 },
 "kind_tornado": {
  "pt": "Tornado (Majuub)",
  "es": "Tornado (Majuub)",
  "en": "Tornado (Majuub)"
 },
 "kind_aura_ff": {
  "pt": "Final Flash",
  "es": "Final Flash",
  "en": "Final Flash"
 },
 "kind_aura_tornado": {
  "pt": "Tornado (Majuub)",
  "es": "Tornado (Majuub)",
  "en": "Tornado (Majuub)"
 },
 "sec_flags": {
  "pt": "Flags (byte +0x00) — some os valores",
  "es": "Flags (byte +0x00) — se suman los valores",
  "en": "Flags (byte +0x00) — values add up"
 },
 "flag_1": {
  "pt": "Desconhecido",
  "es": "Desconocido",
  "en": "Unknown"
 },
 "flag_2": {
  "pt": "Parece ligado a efeitos lançados (como o raio do Kame)",
  "es": "Parece relacionado con efectos lanzados (como el rayo del Kame)",
  "en": "Seems related to thrown effects (like the Kame beam)"
 },
 "flag_4": {
  "pt": "Desconhecido",
  "es": "Desconocido",
  "en": "Unknown"
 },
 "flag_8": {
  "pt": "Usa os ossos dos parâmetros em vez do osso da animação",
  "es": "Usa los huesos de los parámetros en vez del hueso de la animación",
  "en": "Uses the parameters' bones instead of the animation bone"
 },
 "flag_16": {
  "pt": "Desconhecido",
  "es": "Desconocido",
  "en": "Unknown"
 },
 "flag_32": {
  "pt": "Sempre na frente da câmera (não pode ser coberto)",
  "es": "Siempre delante de la cámara (no se puede tapar)",
  "en": "Always in front of the camera (can't be covered)"
 },
 "flag_64": {
  "pt": "Mantém a posição do efeito fixa",
  "es": "Mantiene fija la posición del efecto",
  "en": "Keeps the effect's position fixed"
 },
 "flag_128": {
  "pt": "Corrige os anéis bugados do Makankosappo em choque de poderes ou cena",
  "es": "Corrige los anillos bugueados del Makankosappo en choque de poderes o escena",
  "en": "Fixes bugged Makankosappo rings in beam struggles or scenes"
 },
 "h_flags": {
  "pt": "FLAGS DO BYTE +0x00\n\nCada opção tem um valor, e o byte guarda a SOMA das opções ligadas. Ex.: 8 + 32 = 40. É só marcar as caixas que o programa soma sozinho.\n\nExemplos vistos nos efeitos: 0x20 (32) em partes do carregamento, 0x40 (64) nos brilhos do disparo, 0x08 (8) nas auras do Final Flash, 0x88 (8+128) na explosão.\n\nFonte: documentação da comunidade (os itens 'Desconhecido' ainda não foram descobertos).",
  "es": "FLAGS DEL BYTE +0x00\n\nCada opción tiene un valor, y el byte guarda la SUMA de las opciones activas. Ej.: 8 + 32 = 40. Solo marca las casillas y el programa suma solo.\n\nEjemplos vistos: 0x20 (32) en partes de la carga, 0x40 (64) en los brillos del disparo, 0x08 (8) en las auras del Final Flash, 0x88 (8+128) en la explosión.\n\nFuente: documentación de la comunidad (los 'Desconocido' aún no se descubrieron).",
  "en": "BYTE +0x00 FLAGS\n\nEach option has a value, and the byte stores the SUM of the enabled ones. E.g. 8 + 32 = 40. Just check the boxes and the program adds them.\n\nSeen in effects: 0x20 (32) in charge parts, 0x40 (64) in shot glows, 0x08 (8) in Final Flash auras, 0x88 (8+128) in the explosion.\n\nSource: community docs ('Unknown' items not discovered yet)."
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.12\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.12\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.12\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "kind_aura_ssj": {
  "pt": "SSJ (Big Bang Attack)",
  "es": "SSJ (Big Bang Attack)",
  "en": "SSJ (Big Bang Attack)"
 },
 "kind_aura_solar": {
  "pt": "Solar (4 Estrelas)",
  "es": "Solar (4 Estrellas)",
  "en": "Solar (4 Stars)"
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.13\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.13\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.13\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "protected_save": {
  "pt": "Este é um efeito base protegido do projeto e não pode ser salvo sem alterações.\nUse-o como modelo no seu próprio efeito (Comportamento, Combinar, Extras).",
  "es": "Este es un efecto base protegido del proyecto y no se puede guardar sin cambios.\nÚsalo como modelo en tu propio efecto (Comportamiento, Combinar, Extras).",
  "en": "This is a protected base effect of the project and can't be saved unchanged.\nUse it as a template on your own effect (Behavior, Combine, Extras)."
 },
 "kind_rings": {
  "pt": "Argolas (Makankosappo) — só em golpes com feixe",
  "es": "Anillos (Makankosappo) — solo en ataques con rayo",
  "en": "Rings (Makankosappo) — beam moves only"
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.14\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.14\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.14\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "force_color": {
  "pt": "Forçar cor em partes brancas/cinzas:",
  "es": "Forzar color en partes blancas/grises:",
  "en": "Force color on white/gray parts:"
 },
 "tab_aura": {
  "pt": "Formato da aura",
  "es": "Forma del aura",
  "en": "Aura shape"
 },
 "aura_hint": {
  "pt": "Arquivo de aura (01_charge_aura.pak) aberto: só aparecem as abas que servem para auras.",
  "es": "Archivo de aura (01_charge_aura.pak) abierto: solo aparecen las pestañas útiles para auras.",
  "en": "Aura file (01_charge_aura.pak) open: only aura-related tabs are shown."
 },
 "aura_model": {
  "pt": "Formato:",
  "es": "Forma:",
  "en": "Shape:"
 },
 "aura_keep_color": {
  "pt": "Manter a cor da aura atual (pintar o formato novo com ela)",
  "es": "Mantener el color del aura actual (pintar la forma nueva con él)",
  "en": "Keep the current aura's color (paint the new shape with it)"
 },
 "aura_apply": {
  "pt": "Trocar formato da aura",
  "es": "Cambiar forma del aura",
  "en": "Change aura shape"
 },
 "aura_done": {
  "pt": "Formato da aura trocado.",
  "es": "Forma del aura cambiada.",
  "en": "Aura shape changed."
 },
 "info_aura": {
  "pt": "AURAS (EXPERIMENTAL)\n\nO 01_charge_aura.pak usa o mesmo formato de mini-efeitos dos golpes, só que sem os arquivos 00–02: o arquivo de parâmetros é o primeiro. Por isso o programa consegue abrir, colorir e salvar.\n\n• Cores: funciona igual aos golpes. Se a aura for muito branca, use 'Forçar cor'.\n• Formato da aura: troca a aura inteira por um dos formatos (SSJ2, God, Blue, Instinto Superior, Broly Super, Humano) e pinta com a cor da aura atual.\n• Extras: só as seções de aura e de antes do disparo. Como a aura não tem 'disparo', eles entram na fase 0. Ainda não sabemos se o jogo mostra extras na aura; teste.",
  "es": "AURAS (EXPERIMENTAL)\n\nEl 01_charge_aura.pak usa el mismo formato de mini efectos de los ataques, pero sin los archivos 00–02: el archivo de parámetros es el primero. Por eso el programa puede abrir, colorear y guardar.\n\n• Colores: igual que en los ataques. Si el aura es muy blanca, usa 'Forzar color'.\n• Forma del aura: cambia el aura entera por una de las formas (SSJ2, God, Blue, Instinto Superior, Broly Super, Humano) y la pinta con el color del aura actual.\n• Extras: solo las secciones de aura y de antes del disparo. Como el aura no tiene 'disparo', entran en la fase 0. Aún no sabemos si el juego muestra extras en el aura; prueba.",
  "en": "AURAS (EXPERIMENTAL)\n\n01_charge_aura.pak uses the same mini-effect format as moves, but without files 00–02: the parameter file comes first. That's why the program can open, color and save it.\n\n• Colors: same as moves. If the aura is too white, use 'Force color'.\n• Aura shape: swaps the whole aura for one of the shapes (SSJ2, God, Blue, Ultra Instinct, Broly Super, Human) and paints it with the current aura's color.\n• Extras: only the aura and before-the-shot sections. Since auras have no 'shot', they go into phase 0. We don't know yet whether the game shows extras on auras; test it."
 },
 "info_colors_force": {
  "pt": "",
  "es": "",
  "en": ""
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.15\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.15\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.15\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "tab_support": {
  "pt": "Suporte / Skills",
  "es": "Soporte / Skills",
  "en": "Support / Skills"
 },
 "support_hint": {
  "pt": "Efeito de suporte (00_skill_001, 01_skill_002, 00_effect_skill_1, 01_effect_skill_2) aberto. Eles não têm lançamento: aqui você troca o efeito por um dos formatos de suporte.",
  "es": "Efecto de soporte (00_skill_001, 01_skill_002, 00_effect_skill_1, 01_effect_skill_2) abierto. No tienen lanzamiento: aquí cambias el efecto por una de las formas de soporte.",
  "en": "Support effect (00_skill_001, 01_skill_002, 00_effect_skill_1, 01_effect_skill_2) open. They have no launch: here you swap the effect for one of the support shapes."
 },
 "support_apply": {
  "pt": "Trocar pelo formato de suporte",
  "es": "Cambiar por la forma de soporte",
  "en": "Swap for the support shape"
 },
 "support_done": {
  "pt": "Efeito de suporte trocado.",
  "es": "Efecto de soporte cambiado.",
  "en": "Support effect swapped."
 },
 "aura_on_support_warn": {
  "pt": "⚠ EXPERIMENTAL: usar um formato de aura num efeito de suporte. As partes da aura entram no lugar do efeito, mantendo o arquivo no formato de suporte. Teste numa cópia.",
  "es": "⚠ EXPERIMENTAL: usar una forma de aura en un efecto de soporte. Las partes del aura reemplazan el efecto, manteniendo el archivo en formato de soporte. Prueba en una copia.",
  "en": "⚠ EXPERIMENTAL: using an aura shape on a support effect. Aura parts replace the effect, keeping the file in support layout. Test on a copy."
 },
 "goto_title": {
  "pt": "Ir até o adversário (experimental)",
  "es": "Ir hasta el adversario (experimental)",
  "en": "Travel to the opponent (experimental)"
 },
 "goto_attach": {
  "pt": "Prender as partes da fase 1 ao projétil (+0x09 = 03, +0x0A = 05)",
  "es": "Unir las partes de la fase 1 al proyectil (+0x09 = 03, +0x0A = 05)",
  "en": "Attach phase 1 parts to the projectile (+0x09 = 03, +0x0A = 05)"
 },
 "goto_hits": {
  "pt": "Trazer o impacto no adversário (fase 5) da Paralisia Hitto",
  "es": "Traer el impacto en el adversario (fase 5) de la Parálisis Hitto",
  "en": "Bring the on-opponent impact (phase 5) from Hit's Paralysis"
 },
 "goto_apply": {
  "pt": "Fazer ir até o adversário",
  "es": "Hacer ir hasta el adversario",
  "en": "Make it travel to the opponent"
 },
 "goto_done": {
  "pt": "Pronto: mini-efeito tipo 00 (projétil) adicionado, {m} partes presas a ele e {h} partes de impacto trazidas.\nTeste no jogo: é experimental.",
  "es": "Listo: mini efecto tipo 00 (proyectil) añadido, {m} partes unidas a él y {h} partes de impacto traídas.\nPrueba en el juego: es experimental.",
  "en": "Done: type 00 (projectile) mini-effect added, {m} parts attached to it and {h} impact parts brought in.\nTest in game: it's experimental."
 },
 "info_support": {
  "pt": "SUPORTE / SKILLS\n\nOs arquivos 00_skill_001, 01_skill_002, 00_effect_skill_1 e 01_effect_skill_2 usam o mesmo formato dos golpes (com os arquivos 00–02 vazios). A diferença é que quase nunca têm o mini-efeito tipo 00 (o 'projétil'): o efeito acontece no próprio personagem ou direto no adversário.\n\nO programa reconhece esses arquivos pelo nome e mostra só: Cores, Tamanho e tempo, Extras, Suporte/Skills e Formato da aura (experimental).\n\n'Trocar pelo formato de suporte' substitui todos os mini-efeitos pelos do formato escolhido, mantendo o arquivo como suporte, e pinta com a cor atual se a opção estiver marcada.",
  "es": "SOPORTE / SKILLS\n\nLos archivos 00_skill_001, 01_skill_002, 00_effect_skill_1 y 01_effect_skill_2 usan el mismo formato de los ataques (con los archivos 00–02 vacíos). La diferencia es que casi nunca tienen el mini efecto tipo 00 (el 'proyectil'): el efecto ocurre en el propio personaje o directo en el adversario.\n\nEl programa reconoce estos archivos por el nombre y muestra solo: Colores, Tamaño y tiempo, Extras, Soporte/Skills y Forma del aura (experimental).\n\n'Cambiar por la forma de soporte' sustituye todos los mini efectos por los de la forma elegida, manteniendo el archivo como soporte, y lo pinta con el color actual si la opción está marcada.",
  "en": "SUPPORT / SKILLS\n\n00_skill_001, 01_skill_002, 00_effect_skill_1 and 01_effect_skill_2 use the same format as moves (with files 00–02 empty). The difference is they almost never have the type 00 mini-effect (the 'projectile'): the effect happens on the character itself or directly on the opponent.\n\nThe program recognizes these files by name and shows only: Colors, Size & timing, Extras, Support/Skills and Aura shape (experimental).\n\n'Swap for the support shape' replaces all mini-effects with the chosen shape's, keeping the file as support, and paints with the current color if checked."
 },
 "info_goto": {
  "pt": "IR ATÉ O ADVERSÁRIO (EXPERIMENTAL)\n\nComparando a Paralisia Hitto (móvel) com as paralisias da Zangya e do God, a diferença está em três coisas:\n\n1. Ela tem um mini-efeito tipo 00, o mesmo 'controlador de projétil' dos golpes. As outras não têm.\n2. As partes da fase 1 estão presas ao projétil (+0x09 = 03, +0x0A = 05), então viajam junto com ele.\n3. Ela tem partes de impacto na fase 5 (invocação 05 = acerta o adversário).\n\nO botão aplica as três coisas no seu efeito de suporte, copiando o tipo 00 e o impacto da Paralisia Hitto. Cada parte pode ser desligada nas caixas acima.\n\nLembre que o personagem também precisa ter o golpe configurado para lançar; teste numa cópia.",
  "es": "IR HASTA EL ADVERSARIO (EXPERIMENTAL)\n\nComparando la Parálisis Hitto (móvil) con las de Zangya y God, la diferencia está en tres cosas:\n\n1. Tiene un mini efecto tipo 00, el mismo 'controlador de proyectil' de los ataques. Las otras no.\n2. Las partes de la fase 1 están unidas al proyectil (+0x09 = 03, +0x0A = 05), así que viajan con él.\n3. Tiene partes de impacto en la fase 5 (invocación 05 = golpea al adversario).\n\nEl botón aplica las tres cosas a tu efecto de soporte, copiando el tipo 00 y el impacto de la Parálisis Hitto. Cada parte se puede desactivar en las casillas de arriba.\n\nRecuerda que el personaje también debe tener el ataque configurado para lanzar; prueba en una copia.",
  "en": "TRAVEL TO THE OPPONENT (EXPERIMENTAL)\n\nComparing Hit's moving Paralysis with Zangya's and God's, the difference is threefold:\n\n1. It has a type 00 mini-effect, the same 'projectile controller' moves use. The others don't.\n2. Phase 1 parts are attached to the projectile (+0x09 = 03, +0x0A = 05), so they travel with it.\n3. It has impact parts in phase 5 (invoke 05 = hits the opponent).\n\nThe button applies all three to your support effect, copying type 00 and the impact from Hit's Paralysis. Each part can be turned off in the boxes above.\n\nRemember the character must also have the move set up to launch; test on a copy."
 },
 "opa_title": {
  "pt": "Reduzir intensidade / opacidade",
  "es": "Reducir intensidad / opacidad",
  "en": "Reduce intensity / opacity"
 },
 "opa_reduce": {
  "pt": "Reduzir em",
  "es": "Reducir en",
  "en": "Reduce by"
 },
 "opa_alpha": {
  "pt": "Opacidade (canal A das cores)",
  "es": "Opacidad (canal A de los colores)",
  "en": "Opacity (colors' A channel)"
 },
 "opa_bright": {
  "pt": "Brilho (RGB) — deixa o efeito menos 'estourado'",
  "es": "Brillo (RGB) — deja el efecto menos 'quemado'",
  "en": "Brightness (RGB) — makes the effect less blown out"
 },
 "opa_tex": {
  "pt": "Também nas texturas usadas só por essas partes",
  "es": "También en las texturas usadas solo por esas partes",
  "en": "Also textures used only by these parts"
 },
 "opa_phases": {
  "pt": "Fases:",
  "es": "Fases:",
  "en": "Phases:"
 },
 "opa_all": {
  "pt": "Todas",
  "es": "Todas",
  "en": "All"
 },
 "opa_apply": {
  "pt": "Aplicar redução",
  "es": "Aplicar reducción",
  "en": "Apply reduction"
 },
 "opa_done": {
  "pt": "{n} mini-efeitos reduzidos em {p:.0f}%.",
  "es": "{n} mini efectos reducidos en {p:.0f}%.",
  "en": "{n} mini-effects reduced by {p:.0f}%."
 },
 "info_opa": {
  "pt": "REDUZIR INTENSIDADE / OPACIDADE\n\nAlguns efeitos ficam 'estourados' demais (brancos e opacos), o que não é comum nos efeitos originais do BT3.\n\n• Opacidade: diminui o canal A das cores do shader/V00, deixando o efeito mais transparente.\n• Brilho: diminui o RGB. Como muitos efeitos do jogo somam luz na tela, isso também reduz o 'estouro' do branco.\n• Texturas: diminui também o alfa das paletas usadas somente pelas partes escolhidas.\n\nFases: deixe 'Todas' marcado para o efeito inteiro, ou desmarque e escolha as fases (0 = carregamento, 1 = disparo na maioria dos golpes, 4/5 = acerto). A redução é sobre o valor atual: aplicar 30% duas vezes deixa 49% do original. Ctrl+Z desfaz.",
  "es": "REDUCIR INTENSIDAD / OPACIDAD\n\nAlgunos efectos quedan demasiado 'quemados' (blancos y opacos), algo poco común en los efectos originales de BT3.\n\n• Opacidad: baja el canal A de los colores del shader/V00, dejando el efecto más transparente.\n• Brillo: baja el RGB. Como muchos efectos del juego suman luz en pantalla, esto también reduce el 'quemado' del blanco.\n• Texturas: baja también el alfa de las paletas usadas solo por las partes elegidas.\n\nFases: deja 'Todas' para el efecto entero, o desmarca y elige las fases (0 = carga, 1 = disparo en la mayoría, 4/5 = golpe). La reducción es sobre el valor actual: aplicar 30% dos veces deja 49% del original. Ctrl+Z deshace.",
  "en": "REDUCE INTENSITY / OPACITY\n\nSome effects end up too 'blown out' (white and opaque), which is unusual for vanilla BT3 effects.\n\n• Opacity: lowers the A channel of shader/V00 colors, making the effect more transparent.\n• Brightness: lowers RGB. Since many game effects add light to the screen, this also reduces white blow-out.\n• Textures: also lowers the alpha of palettes used only by the chosen parts.\n\nPhases: keep 'All' for the whole effect, or uncheck it and pick phases (0 = charge, 1 = shot in most moves, 4/5 = hit). The reduction applies to the current value: 30% twice leaves 49% of the original. Ctrl+Z undoes."
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.16\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.16\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.16\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "choose": {
  "pt": "Escolher…",
  "es": "Elegir…",
  "en": "Choose…"
 },
 "beh_opt_scene": {
  "pt": "Copiar a cena do modelo, se ele tiver (ex.: Argola Tripla)",
  "es": "Copiar la escena del modelo, si tiene (ej.: Argola Triple)",
  "en": "Copy the template's scene, if any (e.g. Triple Ring)"
 },
 "scene_copied": {
  "pt": "A cena do modelo também foi copiada.",
  "es": "La escena del modelo también se copió.",
  "en": "The template's scene was copied too."
 },
 "pre_title": {
  "pt": "Formatos pré-disparo",
  "es": "Formas pre-disparo",
  "en": "Pre-shot shapes"
 },
 "pre_apply": {
  "pt": "Trocar o carregamento (fase 0) por este formato",
  "es": "Cambiar la carga (fase 0) por esta forma",
  "en": "Replace the charge (phase 0) with this shape"
 },
 "pre_done": {
  "pt": "{n} mini-efeitos de pré-disparo aplicados na fase 0.",
  "es": "{n} mini efectos de pre-disparo aplicados en la fase 0.",
  "en": "{n} pre-shot mini-effects applied to phase 0."
 },
 "info_pre": {
  "pt": "FORMATOS PRÉ-DISPARO (EXPERIMENTAL)\n\nTrocam só o que acontece antes do disparo (fase 0), mantendo o disparo do seu efeito. Os extras que você já adicionou continuam.\n\nCortes Trunks: são os clarões dos cortes de espada em sequência (cada um com um atraso maior: 7, 11, 16, 25), tirados do efeito Cortes de Espada. Eles passam para a fase 0 e ficam presos ao personagem.",
  "es": "FORMAS PRE-DISPARO (EXPERIMENTAL)\n\nCambian solo lo que ocurre antes del disparo (fase 0), manteniendo el disparo de tu efecto. Los extras que ya añadiste siguen.\n\nCortes Trunks: son los destellos de los cortes de espada en secuencia (cada uno con más retraso: 7, 11, 16, 25), tomados del efecto Cortes de Espada. Pasan a la fase 0 unidos al personaje.",
  "en": "PRE-SHOT SHAPES (EXPERIMENTAL)\n\nThey replace only what happens before the shot (phase 0), keeping your effect's shot. Extras you added stay.\n\nTrunks Slashes: the sequential sword-slash flashes (each with a longer delay: 7, 11, 16, 25), taken from the Sword Slashes effect. They move to phase 0 attached to the character."
 },
 "tab_sparams": {
  "pt": "Parâmetros de suporte",
  "es": "Parámetros de soporte",
  "en": "Support parameters"
 },
 "sparams_hint": {
  "pt": "Características que você pode aplicar em qualquer efeito de suporte, sem trocar o visual.",
  "es": "Características que puedes aplicar a cualquier efecto de soporte, sin cambiar lo visual.",
  "en": "Traits you can apply to any support effect without changing its visuals."
 },
 "goto_title": {
  "pt": "Disparar até o adversário (Hitto) — experimental",
  "es": "Disparar hasta el adversario (Hitto) — experimental",
  "en": "Shoot to the opponent (Hit) — experimental"
 },
 "goto_attach": {
  "pt": "Partes da fase 1 viajam com o projétil (encaixe 03 05)",
  "es": "Partes de la fase 1 viajan con el proyectil (encaje 03 05)",
  "en": "Phase 1 parts travel with the projectile (slot 03 05)"
 },
 "goto_zero": {
  "pt": "Zerar os atrasos dessas partes (evita o efeito aparecer depois do projétil)",
  "es": "Poner en cero los retrasos de esas partes (evita que el efecto aparezca después del proyectil)",
  "en": "Zero those parts' delays (keeps the effect from showing after the projectile)"
 },
 "goto_impact": {
  "pt": "Em vez de viajar, mostrar essas partes no acerto (fase 5)",
  "es": "En vez de viajar, mostrar esas partes en el golpe (fase 5)",
  "en": "Instead of traveling, show those parts on hit (phase 5)"
 },
 "goto_hits": {
  "pt": "Trazer também o impacto visual da Paralisia Hitto",
  "es": "Traer también el impacto visual de la Parálisis Hitto",
  "en": "Also bring Hit's Paralysis visual impact"
 },
 "goto_done": {
  "pt": "Pronto: projétil (tipo 00) e parâmetros de disparo do Hitto aplicados; {m} partes ajustadas, {h} partes de impacto trazidas.\nTeste no jogo: é experimental.",
  "es": "Listo: proyectil (tipo 00) y parámetros de disparo de Hitto aplicados; {m} partes ajustadas, {h} partes de impacto traídas.\nPrueba en el juego: es experimental.",
  "en": "Done: projectile (type 00) and Hit's shooting parameters applied; {m} parts adjusted, {h} impact parts brought.\nTest in game: it's experimental."
 },
 "info_goto": {
  "pt": "DISPARAR ATÉ O ADVERSÁRIO (EXPERIMENTAL)\n\nPor que a versão anterior não funcionava: ela copiava o mini-efeito tipo 00 (o projétil), mas não os PARÂMETROS DO CABEÇALHO do arquivo de parâmetros. Quando você trocava pelo estilo Hitto inteiro, o cabeçalho vinha junto, e por isso funcionava. Agora a função copia: tipo 00 + cabeçalho (bytes 0x06 a 0x3F) da Paralisia Hitto.\n\nPor que o efeito do Taiyoken aparecia depois: o clarão do Taiyoken tem ATRASO 6 (e a flag 16). Com o projétil, ele nasce 6 tempos depois e o projétil já passou do personagem. A opção 'Zerar os atrasos' resolve o visual. Outra opção é mostrar o clarão no acerto (fase 5).\n\nImportante: o efeito de CEGAR em si (o status) é do parâmetro do golpe no personagem, não do eff. Se o status continuar atrasado, o tempo dele precisa ser ajustado no personagem.",
  "es": "DISPARAR HASTA EL ADVERSARIO (EXPERIMENTAL)\n\nPor qué la versión anterior no funcionaba: copiaba el mini efecto tipo 00 (el proyectil), pero no los PARÁMETROS DEL ENCABEZADO del archivo de parámetros. Al cambiar por el estilo Hitto entero, el encabezado venía junto, por eso funcionaba. Ahora la función copia: tipo 00 + encabezado (bytes 0x06 a 0x3F) de la Parálisis Hitto.\n\nPor qué el efecto del Taiyoken aparecía después: el destello del Taiyoken tiene RETRASO 6 (y la flag 16). Con el proyectil, nace 6 tiempos después y el proyectil ya pasó al personaje. La opción 'Poner en cero los retrasos' resuelve lo visual. Otra opción es mostrar el destello en el golpe (fase 5).\n\nImportante: el efecto de CEGAR en sí (el estado) es del parámetro del ataque en el personaje, no del eff. Si el estado sigue con retraso, su tiempo debe ajustarse en el personaje.",
  "en": "SHOOT TO THE OPPONENT (EXPERIMENTAL)\n\nWhy the previous version didn't work: it copied the type 00 mini-effect (the projectile) but not the HEADER PARAMETERS of the parameter file. When you swapped to the whole Hit style, the header came along, which is why that worked. Now the function copies: type 00 + header (bytes 0x06 to 0x3F) from Hit's Paralysis.\n\nWhy the Solar Flare effect showed late: its flash has DELAY 6 (and flag 16). With the projectile, it spawns 6 ticks later, after the projectile already passed the character. 'Zero the delays' fixes the visuals. Another option is showing the flash on hit (phase 5).\n\nImportant: the BLIND effect itself (the status) comes from the move parameter on the character, not the eff. If the status is still late, its timing must be set on the character."
 },
 "persist_title": {
  "pt": "Ficar até usar um especial — experimental",
  "es": "Quedarse hasta usar un especial — experimental",
  "en": "Stay until a special is used — experimental"
 },
 "persist_on": {
  "pt": "Ligar (byte +0x0B = 04)",
  "es": "Activar (byte +0x0B = 04)",
  "en": "Turn on (byte +0x0B = 04)"
 },
 "persist_off": {
  "pt": "Desligar",
  "es": "Desactivar",
  "en": "Turn off"
 },
 "persist_done": {
  "pt": "{n} mini-efeitos marcados para ficar ativos (byte +0x0B = 04).",
  "es": "{n} mini efectos marcados para quedar activos (byte +0x0B = 04).",
  "en": "{n} mini-effects set to stay active (byte +0x0B = 04)."
 },
 "persist_undone": {
  "pt": "{n} mini-efeitos revisados; o 04 foi retirado onde existia.",
  "es": "{n} mini efectos revisados; el 04 se quitó donde existía.",
  "en": "{n} mini-effects checked; 04 removed where present."
 },
 "info_persist": {
  "pt": "FICAR ATÉ USAR UM ESPECIAL (EXPERIMENTAL)\n\nComparei as duas 'auras até usar especial' com os outros suportes e com as auras de carregamento. O ponto em comum é o byte +0x0B dos mini-efeitos: nas duas auras quase tudo tem 04, e as auras de carregamento (que ficam ativas enquanto você carrega) também usam 04. Nos golpes normais esse byte é 00 ou 01.\n\nPor isso a hipótese é: 04 = 'o mini-efeito continua enquanto o estado estiver ativo'. O botão coloca 04 nas fases escolhidas.\n\nA duração real do estado (até usar um especial) provavelmente vem do parâmetro da skill no personagem; aqui controlamos só o visual ficar ou não.",
  "es": "QUEDARSE HASTA USAR UN ESPECIAL (EXPERIMENTAL)\n\nComparé las dos 'auras hasta usar especial' con los otros soportes y con las auras de carga. Lo común es el byte +0x0B de los mini efectos: en las dos auras casi todo tiene 04, y las auras de carga (que siguen activas mientras cargas) también usan 04. En los ataques normales ese byte es 00 o 01.\n\nHipótesis: 04 = 'el mini efecto continúa mientras el estado esté activo'. El botón pone 04 en las fases elegidas.\n\nLa duración real del estado (hasta usar un especial) probablemente viene del parámetro de la skill en el personaje; aquí solo controlamos si lo visual se queda.",
  "en": "STAY UNTIL A SPECIAL IS USED (EXPERIMENTAL)\n\nI compared both 'auras until special' with the other supports and the charge auras. What they share is the mini-effects' byte +0x0B: in both auras almost everything has 04, and charge auras (active while you charge) also use 04. In normal moves that byte is 00 or 01.\n\nHypothesis: 04 = 'the mini-effect keeps going while the state is active'. The button sets 04 on the chosen phases.\n\nThe state's real duration (until a special is used) probably comes from the skill parameter on the character; here we only control whether the visuals stay."
 },
 "hdr_title": {
  "pt": "Parâmetros de cada suporte (cabeçalho)",
  "es": "Parámetros de cada soporte (encabezado)",
  "en": "Each support's parameters (header)"
 },
 "hdr_from": {
  "pt": "Copiar de:",
  "es": "Copiar de:",
  "en": "Copy from:"
 },
 "hdr_param": {
  "pt": "Parâmetro",
  "es": "Parámetro",
  "en": "Parameter"
 },
 "hdr_done": {
  "pt": "Parâmetros de '{n}' aplicados.",
  "es": "Parámetros de '{n}' aplicados.",
  "en": "'{n}' parameters applied."
 },
 "info_hdr": {
  "pt": "PARÂMETROS DE CADA SUPORTE\n\nCada suporte guarda valores próprios no cabeçalho do arquivo de parâmetros (byte 0x06 e 14 números de 0x08 a 0x3C). Exemplos:\n• Paralisia Zangya: 8, 25, 25, 1, 0.5 …\n• Barreira Andróide: 10, 11.8, 12, 1, 0.5\n• Explosive Wave: 11, 12, 15, 0.5, 0.7\n• Paralisia Hitto: 0.5 … 80\n• Taiyoken: 5 … 0.8\nO significado exato de cada um ainda não foi descoberto (parecem alcance/tamanho e tempos). 'Copiar de' traz todos os valores de um suporte; abaixo você pode editar um a um.",
  "es": "PARÁMETROS DE CADA SOPORTE\n\nCada soporte guarda valores propios en el encabezado del archivo de parámetros (byte 0x06 y 14 números de 0x08 a 0x3C). Ejemplos:\n• Parálisis Zangya: 8, 25, 25, 1, 0.5 …\n• Barrera Androide: 10, 11.8, 12, 1, 0.5\n• Explosive Wave: 11, 12, 15, 0.5, 0.7\n• Parálisis Hitto: 0.5 … 80\n• Taiyoken: 5 … 0.8\nEl significado exacto de cada uno aún no se descubrió (parecen alcance/tamaño y tiempos). 'Copiar de' trae todos los valores de un soporte; abajo puedes editar uno a uno.",
  "en": "EACH SUPPORT'S PARAMETERS\n\nEach support stores its own values in the parameter file header (byte 0x06 and 14 numbers from 0x08 to 0x3C). Examples:\n• Zangya Paralysis: 8, 25, 25, 1, 0.5 …\n• Android Barrier: 10, 11.8, 12, 1, 0.5\n• Explosive Wave: 11, 12, 15, 0.5, 0.7\n• Hit Paralysis: 0.5 … 80\n• Solar Flare: 5 … 0.8\nThe exact meaning of each isn't known yet (they look like range/size and timings). 'Copy from' brings all of a support's values; below you can edit them one by one."
 },
 "grow_title": {
  "pt": "Padrões de crescimento",
  "es": "Patrones de crecimiento",
  "en": "Growth patterns"
 },
 "grow_turles": {
  "pt": "Argola Turles (nasce e cresce)",
  "es": "Anillo Turles (nace y crece)",
  "en": "Turles Ring (spawns and grows)"
 },
 "grow_bills": {
  "pt": "Ulti Bills (contrai e explode)",
  "es": "Ulti Bills (se contrae y explota)",
  "en": "Beerus Ult (shrinks then explodes)"
 },
 "grow_reverse": {
  "pt": "Reverter (diminuir em vez de crescer)",
  "es": "Invertir (achicar en vez de crecer)",
  "en": "Reverse (shrink instead of grow)"
 },
 "grow_marked": {
  "pt": "Aplicar nos marcados",
  "es": "Aplicar a los marcados",
  "en": "Apply to checked"
 },
 "grow_group": {
  "pt": "Aplicar no grupo",
  "es": "Aplicar al grupo",
  "en": "Apply to group"
 },
 "info_grow": {
  "pt": "PADRÕES DE CRESCIMENTO\n\nTirados dos efeitos originais, usando os tamanhos 1, 2 e 3 e os tempos entre eles:\n• Argola Turles: antes do disparo, a argola nasce do zero, vai para a metade em 0,2 e chega ao tamanho total em mais 0,5.\n• Ulti Bills: contrai até quase nada e depois explode até o tamanho total (tempos 0,5 e 1,2).\n\nO tamanho máximo de cada mini-efeito é mantido; só muda o caminho até ele. 'Reverter' faz o caminho ao contrário (ex.: a argola começa grande e some).",
  "es": "PATRONES DE CRECIMIENTO\n\nTomados de los efectos originales, usando los tamaños 1, 2 y 3 y los tiempos entre ellos:\n• Anillo Turles: antes del disparo, el anillo nace de cero, llega a la mitad en 0,2 y al tamaño total en 0,5 más.\n• Ulti Bills: se contrae casi a nada y luego explota hasta el tamaño total (tiempos 0,5 y 1,2).\n\nSe mantiene el tamaño máximo de cada mini efecto; solo cambia el camino. 'Invertir' hace el camino al revés (ej.: el anillo empieza grande y desaparece).",
  "en": "GROWTH PATTERNS\n\nTaken from the original effects, using sizes 1, 2 and 3 and the times between them:\n• Turles Ring: before the shot, the ring spawns from zero, reaches half in 0.2 and full size after 0.5 more.\n• Beerus Ult: shrinks to almost nothing, then explodes to full size (times 0.5 and 1.2).\n\nEach mini-effect's maximum size is kept; only the path changes. 'Reverse' plays it backwards (e.g. the ring starts big and vanishes)."
 },
 "kind_aura_trails": {
  "pt": "Rastros de aura no chão (Kamehameha Pai e Filho)",
  "es": "Rastros de aura en el suelo (Kamehameha Padre e Hijo)",
  "en": "Aura trails on the ground (Father-Son Kamehameha)"
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.17\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.17\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.17\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "slot_aura": {
  "pt": "Aura",
  "es": "Aura",
  "en": "Aura"
 },
 "kind_aura_trails": {
  "pt": "Rastros de aura (Kamehameha Pai e Filho)",
  "es": "Rastros de aura (Kamehameha Padre e Hijo)",
  "en": "Aura trails (Father-Son Kamehameha)"
 },
 "kind_broly_ring": {
  "pt": "Anel (Projéteis Broly)",
  "es": "Anillo (Proyectiles Broly)",
  "en": "Ring (Broly projectiles)"
 },
 "warn_magic344": {
  "pt": "Cortes de Trunks: para a cor do corte mudar, coloque 344 em 'Magic Word' no parâmetro do ataque.\nSem isso, os cortes usam uma cor global.",
  "es": "Cortes de Trunks: para que cambie el color del corte, pon 344 en 'Magic Word' en el parámetro del ataque.\nSin eso, los cortes usan un color global.",
  "en": "Trunks slashes: for the slash color to change, set 'Magic Word' to 344 in the move parameter.\nOtherwise the slashes use a global color."
 },
 "warn_params": {
  "pt": "Espada de Ki: este formato precisa dos parâmetros do golpe configurados no personagem para funcionar corretamente.",
  "es": "Espada de Ki: esta forma necesita los parámetros del ataque configurados en el personaje para funcionar bien.",
  "en": "Ki Sword: this shape needs the move parameters set on the character to work correctly."
 },
 "warn_scene_only": {
  "pt": "Paralisia General Blue: este efeito não tem mini-efeitos; ele é só a cena (o modelo 3D vem do jogo). Aplicar este formato copia só a cena.",
  "es": "Parálisis General Blue: este efecto no tiene mini efectos; es solo la escena (el modelo 3D viene del juego). Aplicar esta forma copia solo la escena.",
  "en": "General Blue Paralysis: this effect has no mini-effects; it's only the scene (the 3D model comes from the game). Applying it copies only the scene."
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.18\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.18\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.18\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "nerf_title": {
  "pt": "Reduzir cores das texturas",
  "es": "Reducir colores de las texturas",
  "en": "Reduce texture colors"
 },
 "nerf_to": {
  "pt": "Reduzir para:",
  "es": "Reducir a:",
  "en": "Reduce to:"
 },
 "nerf_lv16": {
  "pt": "16 cores (arquivo fica mais leve)",
  "es": "16 colores (archivo más liviano)",
  "en": "16 colors (smaller file)"
 },
 "nerf_lvN": {
  "pt": "{n} cores (só visual)",
  "es": "{n} colores (solo visual)",
  "en": "{n} colors (visual only)"
 },
 "nerf_doneN": {
  "pt": "{n} imagens reduzidas para {c} cores.\nTamanho: {b:.0f} KB → {a:.0f} KB",
  "es": "{n} imágenes reducidas a {c} colores.\nTamaño: {b:.0f} KB → {a:.0f} KB",
  "en": "{n} images reduced to {c} colors.\nSize: {b:.0f} KB → {a:.0f} KB"
 },
 "info_nerf": {
  "pt": "REDUZIR CORES\n\nO programa nunca muda a quantidade de cores sozinho; só este botão faz isso.\n\n• 16 cores: converte as texturas de 256 cores para o formato de 16 cores (4 bits por pixel), que o jogo já usa em várias texturas. O desenho cai pela metade e a paleta de 1 KB para 64 bytes: é a opção que deixa o ARQUIVO MAIS LEVE (Madam: 153 KB → 86 KB).\n\n• 128, 64 e 32 cores: reduzem as cores usadas, mas a textura continua no formato de 256 cores (1 byte por pixel e paleta de 256 posições). O arquivo NÃO fica menor; a diferença é só visual (menos tons, visual mais 'chapado'). O formato do PS2 só tem 16 ou 256 cores, por isso não existe um tamanho intermediário.\n\nA redução escolhe as cores que melhor representam cada imagem. Brilhos e degradês podem ganhar 'degraus'. Ctrl+Z desfaz.",
  "es": "REDUCIR COLORES\n\nEl programa nunca cambia la cantidad de colores por su cuenta; solo este botón lo hace.\n\n• 16 colores: convierte las texturas de 256 colores al formato de 16 (4 bits por píxel), que el juego ya usa en varias texturas. El dibujo se reduce a la mitad y la paleta de 1 KB a 64 bytes: es la opción que deja el ARCHIVO MÁS LIVIANO (Madam: 153 KB → 86 KB).\n\n• 128, 64 y 32 colores: reducen los colores usados, pero la textura sigue en el formato de 256 (1 byte por píxel y paleta de 256). El archivo NO queda más chico; la diferencia es solo visual (menos tonos). El formato de PS2 solo tiene 16 o 256 colores, por eso no hay un tamaño intermedio.\n\nLa reducción elige los colores que mejor representan cada imagen. Brillos y degradados pueden quedar escalonados. Ctrl+Z deshace.",
  "en": "REDUCE COLORS\n\nThe program never changes color count by itself; only this button does.\n\n• 16 colors: converts 256-color textures to the 16-color format (4 bits per pixel), which the game already uses for many textures. Pixel data halves and the palette drops from 1 KB to 64 bytes: this is the option that makes the FILE SMALLER (Madam: 153 KB → 86 KB).\n\n• 128, 64 and 32 colors: reduce the colors used, but the texture stays in the 256-color format (1 byte per pixel, 256-entry palette). The file does NOT get smaller; the difference is visual only. PS2 formats only have 16 or 256 colors, so there's no in-between size.\n\nThe reduction picks the colors that best represent each image. Glows and gradients may band. Ctrl+Z undoes."
 },
 "tab_flags": {
  "pt": "Flags",
  "es": "Flags",
  "en": "Flags"
 },
 "flags_hint": {
  "pt": "Marque as flags do byte +0x00 e escolha onde aplicar. 'Ligar' acrescenta as marcadas, 'Desligar' tira, e 'Definir' deixa o byte exatamente igual às marcadas.",
  "es": "Marca las flags del byte +0x00 y elige dónde aplicarlas. 'Activar' agrega las marcadas, 'Desactivar' las quita y 'Definir' deja el byte exactamente como las marcadas.",
  "en": "Check byte +0x00 flags and choose where to apply them. 'Turn on' adds the checked ones, 'Turn off' removes them, and 'Set' makes the byte exactly the checked ones."
 },
 "flags_target": {
  "pt": "Aplicar em:",
  "es": "Aplicar en:",
  "en": "Apply to:"
 },
 "flags_t_marked": {
  "pt": "Mini-efeitos marcados na lista",
  "es": "Mini efectos marcados en la lista",
  "en": "Checked mini-effects in the list"
 },
 "flags_t_all": {
  "pt": "Todos os mini-efeitos",
  "es": "Todos los mini efectos",
  "en": "All mini-effects"
 },
 "flags_t_phases": {
  "pt": "Fases:",
  "es": "Fases:",
  "en": "Phases:"
 },
 "flags_on": {
  "pt": "Ligar",
  "es": "Activar",
  "en": "Turn on"
 },
 "flags_off": {
  "pt": "Desligar",
  "es": "Desactivar",
  "en": "Turn off"
 },
 "flags_set": {
  "pt": "Definir",
  "es": "Definir",
  "en": "Set"
 },
 "flags_read": {
  "pt": "Ler as flags do mini-efeito selecionado",
  "es": "Leer las flags del mini efecto seleccionado",
  "en": "Read flags from the selected mini-effect"
 },
 "flags_done": {
  "pt": "{n} mini-efeitos alterados (flags: {v}).",
  "es": "{n} mini efectos modificados (flags: {v}).",
  "en": "{n} mini-effects changed (flags: {v})."
 },
 "flags_sel": {
  "pt": "Mini-efeito selecionado: byte +0x00 = {v}",
  "es": "Mini efecto seleccionado: byte +0x00 = {v}",
  "en": "Selected mini-effect: byte +0x00 = {v}"
 }
})

T.update({
 "about_text": {
  "pt": "BT3 Effect Studio v0.19\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "BT3 Effect Studio v0.19\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "BT3 Effect Studio v0.19\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "nerf_title": {
  "pt": "Reduzir cores das texturas (256 → 16)",
  "es": "Reducir colores de las texturas (256 → 16)",
  "en": "Reduce texture colors (256 → 16)"
 },
 "flags_hint2": {
  "pt": "Flags do 03.dat: é o primeiro byte das 4 primeiras linhas de parâmetros (o primeiro bloco depois das categorias). Marque as opções e clique em Aplicar; os valores são somados sozinhos.",
  "es": "Flags del 03.dat: es el primer byte de las 4 primeras filas de parámetros (el primer bloque después de las categorías). Marca las opciones y haz clic en Aplicar; los valores se suman solos.",
  "en": "03.dat flags: the first byte of the first 4 parameter rows (the first block after the categories). Check the options and click Apply; values add up automatically."
 },
 "flags_cur": {
  "pt": "Valor atual: {v}   →   novo: {n}",
  "es": "Valor actual: {v}   →   nuevo: {n}",
  "en": "Current value: {v}   →   new: {n}"
 },
 "flags_none": {
  "pt": "Este efeito não tem blocos de parâmetros.",
  "es": "Este efecto no tiene bloques de parámetros.",
  "en": "This effect has no parameter blocks."
 }
})

T.update({
 "app_title": {
  "pt": "Effects Max Ultra Legendary Studios",
  "es": "Effects Max Ultra Legendary Studios",
  "en": "Effects Max Ultra Legendary Studios"
 },
 "about_text": {
  "pt": "Effects Max Ultra Legendary Studios v1.0\n(antigo BT3 Effect Studio)\nEditor de efeitos de Budokai Tenkaichi 3.\nFeito por Ariel Sofia e Kaya.",
  "es": "Effects Max Ultra Legendary Studios v1.0\n(antes BT3 Effect Studio)\nEditor de efectos de Budokai Tenkaichi 3.\nHecho por Ariel Sofia y Kaya.",
  "en": "Effects Max Ultra Legendary Studios v1.0\n(formerly BT3 Effect Studio)\nBudokai Tenkaichi 3 effect editor.\nMade by Ariel Sofia and Kaya."
 },
 "col_type": {
  "pt": "Classe",
  "es": "Clase",
  "en": "Class"
 },
 "g_impact": {
  "pt": "Grupos 04/05",
  "es": "Grupos 04/05",
  "en": "Groups 04/05"
 },
 "tools": {
  "pt": "Ferramentas",
  "es": "Herramientas",
  "en": "Tools"
 },
 "btn_textures": {
  "pt": "Texturas…",
  "es": "Texturas…",
  "en": "Textures…"
 },
 "btn_hex": {
  "pt": "Hexadecimal…",
  "es": "Hexadecimal…",
  "en": "Hex…"
 },
 "hex_external": {
  "pt": "Abrir .dat avulso em hexadecimal…",
  "es": "Abrir .dat suelto en hexadecimal…",
  "en": "Open loose .dat in hex…"
 },
 "btn_classes": {
  "pt": "ⓘ Classes e grupos",
  "es": "ⓘ Clases y grupos",
  "en": "ⓘ Classes and groups"
 },
 "summary_minis": {
  "pt": "Mini-efeitos",
  "es": "Mini efectos",
  "en": "Mini-effects"
 },
 "kind_skill": {
  "pt": "Golpe",
  "es": "Ataque",
  "en": "Move"
 },
 "kind_aura": {
  "pt": "Aura",
  "es": "Aura",
  "en": "Aura"
 },
 "kind_support": {
  "pt": "Suporte",
  "es": "Soporte",
  "en": "Support"
 },
 "cont_title": {
  "pt": "Pacote de efeitos: {n}",
  "es": "Paquete de efectos: {n}",
  "en": "Effects package: {n}"
 },
 "cont_hint": {
  "pt": "Este é um pacote completo de efeitos do personagem. Escolha qual efeito abrir. Ao salvar, o efeito volta para dentro deste mesmo pacote (com backup .bak). 'Salvar como' salva só o efeito, separado.",
  "es": "Este es un paquete completo de efectos del personaje. Elige qué efecto abrir. Al guardar, el efecto vuelve dentro de este mismo paquete (con copia .bak). 'Guardar como' guarda solo el efecto, aparte.",
  "en": "This is a character's full effects package. Choose which effect to open. Saving puts the effect back inside this same package (with a .bak backup). 'Save as' saves only the effect, separately."
 },
 "cont_kind": {
  "pt": "Tipo",
  "es": "Tipo",
  "en": "Kind"
 },
 "cont_open": {
  "pt": "Abrir efeito",
  "es": "Abrir efecto",
  "en": "Open effect"
 },
 "cont_saved": {
  "pt": "{n} salvo dentro de {c}.",
  "es": "{n} guardado dentro de {c}.",
  "en": "{n} saved inside {c}."
 },
 "color_contrast": {
  "pt": "Colorir com contraste…",
  "es": "Colorear con contraste…",
  "en": "Color with contrast…"
 },
 "contrast_shift": {
  "pt": "desvio (°):",
  "es": "desvío (°):",
  "en": "shift (°):"
 },
 "contrast_done": {
  "pt": "Pronto. Partes secundárias pintadas com {c}.",
  "es": "Listo. Partes secundarias pintadas con {c}.",
  "en": "Done. Secondary parts painted with {c}."
 },
 "info_contrast": {
  "pt": "COLORIR COM CONTRASTE\n\nO jogo original não pinta tudo com uma cor só: efeitos roxos têm partes azuladas, laranjas têm partes avermelhadas. Isso ajuda a distinguir as camadas.\n\nVocê escolhe a cor principal; as partes secundárias recebem uma cor 'vizinha' com o tom deslocado (padrão -35°: roxo → azul, laranja → vermelho; use valores positivos para o lado contrário).\n\nSão tratadas como secundárias: as partes que no original já tinham um tom diferente do predominante, e as classes 12 (raios) e 10 (iluminação).",
  "es": "COLOREAR CON CONTRASTE\n\nEl juego original no pinta todo de un solo color: efectos morados tienen partes azuladas, naranjas tienen partes rojizas. Ayuda a distinguir las capas.\n\nEliges el color principal; las partes secundarias reciben un color 'vecino' con el tono desplazado (por defecto -35°: morado → azul, naranja → rojo; usa valores positivos para el otro lado).\n\nSon secundarias: las partes que en el original ya tenían un tono distinto del predominante, y las clases 12 (rayos) y 10 (iluminación).",
  "en": "COLOR WITH CONTRAST\n\nThe original game doesn't paint everything one color: purple effects have bluish parts, orange ones have reddish parts. It helps tell layers apart.\n\nYou pick the main color; secondary parts get a 'neighbor' color with shifted hue (default -35°: purple → blue, orange → red; use positive values for the other side).\n\nSecondary parts are those that already had a different hue in the original, plus classes 12 (lightning) and 10 (lighting)."
 },
 "channels": {
  "pt": "Canais RGB:",
  "es": "Canales RGB:",
  "en": "RGB channels:"
 },
 "ch_swap": {
  "pt": "Inverter",
  "es": "Invertir",
  "en": "Swap"
 },
 "ch_copy": {
  "pt": "Copiar",
  "es": "Copiar",
  "en": "Copy"
 },
 "ch_scope_sel": {
  "pt": "selecionado",
  "es": "seleccionado",
  "en": "selected"
 },
 "ch_scope_marked": {
  "pt": "marcados",
  "es": "marcados",
  "en": "checked"
 },
 "ch_scope_all": {
  "pt": "todos",
  "es": "todos",
  "en": "all"
 },
 "stripes_hide": {
  "pt": "Ocultar listras brancas globais",
  "es": "Ocultar rayas blancas globales",
  "en": "Hide global white stripes"
 },
 "stripes_show": {
  "pt": "Mostrar listras",
  "es": "Mostrar rayas",
  "en": "Show stripes"
 },
 "stripes_none": {
  "pt": "Este efeito não tem o mini-efeito global (classe 00).",
  "es": "Este efecto no tiene el mini efecto global (clase 00).",
  "en": "This effect has no global mini-effect (class 00)."
 },
 "info_stripes": {
  "pt": "LISTRAS BRANCAS GLOBAIS\n\nO primeiro mini-efeito de todo 03_.dat (classe 00) é um efeito GLOBAL de listras brancas, guardado nos arquivos globais do jogo. Ele não pode ser removido, mas zerando os floats de tamanho ele deixa de aparecer. 'Mostrar listras' devolve o tamanho padrão (0,15).",
  "es": "RAYAS BLANCAS GLOBALES\n\nEl primer mini efecto de todo 03_.dat (clase 00) es un efecto GLOBAL de rayas blancas, guardado en los archivos globales del juego. No se puede quitar, pero poniendo en cero los floats de tamaño deja de verse. 'Mostrar rayas' devuelve el tamaño por defecto (0,15).",
  "en": "GLOBAL WHITE STRIPES\n\nThe first mini-effect of every 03_.dat (class 00) is a GLOBAL white-stripes effect stored in the game's global files. It can't be removed, but zeroing its size floats hides it. 'Show stripes' restores the default size (0.15)."
 },
 "barrage_on": {
  "pt": "Converter em barragem",
  "es": "Convertir en barrera",
  "en": "Convert to barrage"
 },
 "barrage_off": {
  "pt": "Tirar modo barragem",
  "es": "Quitar modo barrera",
  "en": "Remove barrage mode"
 },
 "barrage_state_on": {
  "pt": "Modo barragem: LIGADO",
  "es": "Modo barrera: ACTIVADO",
  "en": "Barrage mode: ON"
 },
 "barrage_state_off": {
  "pt": "Modo barragem: desligado",
  "es": "Modo barrera: desactivado",
  "en": "Barrage mode: off"
 },
 "info_barrage": {
  "pt": "MODO BARRAGEM (byte 0x27 do 03.dat)\n\n02 = o efeito se comporta como barragem (vários disparos); desligado = projétil/feixe único. 03 = barragem que também aparece durante a ceninha (Ultimate do Cui).\n\n'Converter em barragem' deixa qualquer efeito compatível com golpes de múltiplos disparos. O golpe do personagem também precisa ser de barragem.",
  "es": "MODO BARRERA (byte 0x27 del 03.dat)\n\n02 = el efecto se comporta como barrera (varios disparos); apagado = proyectil/rayo único. 03 = barrera que también aparece durante la escena (Ultimate de Cui).\n\n'Convertir en barrera' deja cualquier efecto compatible con ataques de múltiples disparos. El ataque del personaje también debe ser de barrera.",
  "en": "BARRAGE MODE (03.dat byte 0x27)\n\n02 = the effect behaves as a barrage (multiple shots); off = single projectile/beam. 03 = barrage that also shows during the scene (Cui's Ultimate).\n\n'Convert to barrage' makes any effect compatible with multi-shot moves. The character's move must also be a barrage."
 },
 "scene_table_btn": {
  "pt": "Editar 02_.dat por mapa (altura e posição Z)…",
  "es": "Editar 02_.dat por mapa (altura y posición Z)…",
  "en": "Edit 02_.dat per map (height and Z)…"
 },
 "scene_table_hint": {
  "pt": "O 02_.dat define a altura (Y) e a posição Z GLOBAIS dos dois personagens na ceninha, separadamente para cada um dos 35 mapas e para cada um dos 5 eventos possíveis.",
  "es": "El 02_.dat define la altura (Y) y la posición Z GLOBALES de ambos personajes en la escena, por separado para cada uno de los 35 mapas y cada uno de los 5 eventos posibles.",
  "en": "02_.dat sets both characters' GLOBAL height (Y) and Z position in the scene, separately for each of the 35 maps and each of the 5 possible events."
 },
 "scene_map": {
  "pt": "Mapa",
  "es": "Mapa",
  "en": "Map"
 },
 "scene_event": {
  "pt": "Evento",
  "es": "Evento",
  "en": "Event"
 },
 "scene_y": {
  "pt": "Altura (Y)",
  "es": "Altura (Y)",
  "en": "Height (Y)"
 },
 "scene_z": {
  "pt": "Posição Z",
  "es": "Posición Z",
  "en": "Z position"
 },
 "scene_apply_map": {
  "pt": "Aplicar neste mapa",
  "es": "Aplicar en este mapa",
  "en": "Apply to this map"
 },
 "scene_apply_all": {
  "pt": "Aplicar em todos os mapas",
  "es": "Aplicar en todos los mapas",
  "en": "Apply to all maps"
 },
 "appear_title": {
  "pt": "Como o golpe aparece na ceninha",
  "es": "Cómo aparece el ataque en la escena",
  "en": "How the move shows in the scene"
 },
 "appear_none": {
  "pt": "Não aparece",
  "es": "No aparece",
  "en": "Doesn't show"
 },
 "appear_beam": {
  "pt": "Feixe que encerra o golpe (Burst Rush, Nail…)",
  "es": "Rayo que termina el ataque (Burst Rush, Nail…)",
  "en": "Beam that ends the move (Burst Rush, Nail…)"
 },
 "appear_projectile": {
  "pt": "Projétil (Comet Attack, Gotenks Volleyball…)",
  "es": "Proyectil (Comet Attack, Gotenks Volleyball…)",
  "en": "Projectile (Comet Attack, Gotenks Volleyball…)"
 },
 "appear_vertical": {
  "pt": "Feixe vertical: de cima p/ baixo ou de baixo p/ cima (Trunks Dome)",
  "es": "Rayo vertical: de arriba abajo o de abajo arriba (Trunks Dome)",
  "en": "Vertical beam: top-down or bottom-up (Trunks Dome)"
 },
 "appear_barrage": {
  "pt": "Barragem aparece na ceninha (Ultimate do Cui)",
  "es": "La barrera aparece en la escena (Ultimate de Cui)",
  "en": "Barrage shows in the scene (Cui's Ultimate)"
 },
 "appear_need_barrage": {
  "pt": "Para a barragem aparecer na ceninha, o efeito precisa estar convertido em barragem (byte 0x27). Converter agora?",
  "es": "Para que la barrera aparezca en la escena, el efecto debe estar convertido en barrera (byte 0x27). ¿Convertir ahora?",
  "en": "For the barrage to show in the scene, the effect must be converted to barrage (byte 0x27). Convert now?"
 },
 "info_appear": {
  "pt": "APARIÇÃO NA CENINHA (bytes 0x21–0x27 do 03.dat)\n\n• Feixe que encerra o golpe: 0x21 = 01 e 0x26 = 10.\n• Projétil: 0x21 = 01, 0x25 = 05 e 0x26 = 10.\n• Feixe vertical (cima/baixo): 0x21 = 01, 0x22 = 01 e 0x26 = 10 (no Ultimate do Kid Gohan o 0x26 vale 50).\n• Barragem na ceninha: 0x27 = 03 (o efeito precisa ser barragem).\n\nFonte: documentação Madeirada.",
  "es": "APARICIÓN EN LA ESCENA (bytes 0x21–0x27 del 03.dat)\n\n• Rayo que termina el ataque: 0x21 = 01 y 0x26 = 10.\n• Proyectil: 0x21 = 01, 0x25 = 05 y 0x26 = 10.\n• Rayo vertical: 0x21 = 01, 0x22 = 01 y 0x26 = 10 (en el Ultimate de Kid Gohan 0x26 vale 50).\n• Barrera en la escena: 0x27 = 03 (el efecto debe ser barrera).",
  "en": "SCENE APPEARANCE (03.dat bytes 0x21–0x27)\n\n• Beam ending the move: 0x21 = 01 and 0x26 = 10.\n• Projectile: 0x21 = 01, 0x25 = 05 and 0x26 = 10.\n• Vertical beam: 0x21 = 01, 0x22 = 01 and 0x26 = 10 (Kid Gohan's Ultimate uses 50).\n• Barrage in scene: 0x27 = 03 (effect must be a barrage)."
 },
 "persist_scene_title": {
  "pt": "Partes do lançamento (grupo 01) na ceninha",
  "es": "Partes del lanzamiento (grupo 01) en la escena",
  "en": "Launch parts (group 01) in the scene"
 },
 "persist_scene_on": {
  "pt": "Manter durante a ceninha (04)",
  "es": "Mantener durante la escena (04)",
  "en": "Keep during the scene (04)"
 },
 "persist_scene_off": {
  "pt": "Esconder na ceninha (03)",
  "es": "Ocultar en la escena (03)",
  "en": "Hide in the scene (03)"
 },
 "persist_scene_done": {
  "pt": "{n} mini-efeitos do grupo 01 ajustados.",
  "es": "{n} mini efectos del grupo 01 ajustados.",
  "en": "{n} group 01 mini-effects adjusted."
 },
 "info_persist_scene": {
  "pt": "GRUPO 01 NA CENINHA (byte +0x09)\n\nNos mini-efeitos do grupo 01 (lançamento), o byte +0x09 diz se eles continuam durante uma ceninha:\n• 03 = o mini-efeito NÃO aparece na ceninha;\n• 04 = o mini-efeito continua aparecendo na ceninha (é por isso que a rodela do Full Force Kamehameha aparece nela).",
  "es": "GRUPO 01 EN LA ESCENA (byte +0x09)\n\nEn los mini efectos del grupo 01 (lanzamiento), el byte +0x09 indica si siguen durante una escena:\n• 03 = NO aparece en la escena;\n• 04 = sigue apareciendo en la escena (por eso el aro del Full Force Kamehameha aparece en ella).",
  "en": "GROUP 01 IN THE SCENE (byte +0x09)\n\nFor group 01 (launch) mini-effects, byte +0x09 says whether they continue during a scene:\n• 03 = does NOT show in the scene;\n• 04 = keeps showing in the scene (that's why the Full Force Kamehameha ring shows in it)."
 },
 "w_scene_tip": {
  "pt": "O 02_.dat (cena) pesa 2,8 KB. Efeitos que NÃO são ceninha não precisam dele: use 'Sem cena' na aba Cena ao acertar para removê-lo.",
  "es": "El 02_.dat (escena) pesa 2,8 KB. Los efectos que NO son escena no lo necesitan: usa 'Sin escena' en la pestaña Escena al acertar para quitarlo.",
  "en": "02_.dat (scene) weighs 2.8 KB. Effects that are NOT scenes don't need it: use 'No scene' in the Scene on hit tab to remove it."
 },
 "sec_behave": {
  "pt": "Comportamento (bytes +0x09 a +0x0B)",
  "es": "Comportamiento (bytes +0x09 a +0x0B)",
  "en": "Behavior (bytes +0x09 to +0x0B)"
 },
 "p_unk9": {
  "pt": "Permanência (+0x09)",
  "es": "Permanencia (+0x09)",
  "en": "Persistence (+0x09)"
 },
 "p_unkA": {
  "pt": "Posição (+0x0A)",
  "es": "Posición (+0x0A)",
  "en": "Position (+0x0A)"
 },
 "p_unkB": {
  "pt": "Estado (+0x0B)",
  "es": "Estado (+0x0B)",
  "en": "State (+0x0B)"
 },
 "p_invoke": {
  "pt": "Grupo de invocação",
  "es": "Grupo de invocación",
  "en": "Invoke group"
 },
 "h_b9": {
  "pt": "PERMANÊNCIA (+0x09)\n00 = some quando o tempo dele acaba (ex.: 'spark' da aura)\n02 = fica até o lançamento\n03 = no grupo 01, NÃO aparece numa ceninha\n04 = no grupo 01, continua na ceninha",
  "es": "PERMANENCIA (+0x09)\n00 = desaparece al terminar su tiempo\n02 = queda hasta el lanzamiento\n03 = en el grupo 01, NO aparece en la escena\n04 = en el grupo 01, sigue en la escena",
  "en": "PERSISTENCE (+0x09)\n00 = vanishes when its time ends\n02 = stays until the launch\n03 = in group 01, does NOT show in a scene\n04 = in group 01, keeps showing in the scene"
 },
 "h_bA": {
  "pt": "POSIÇÃO (+0x0A)\n01 = estático, invocado na referência (como o grupo 00)\n02 = ao redor do personagem (auras)\n04 = no centro do personagem (iluminação/sombra, classe 10)\n05 = em volta da referência (1º efeito da classe 05), indo até o oponente e perseguindo-o",
  "es": "POSICIÓN (+0x0A)\n01 = estático, en la referencia (como el grupo 00)\n02 = alrededor del personaje (auras)\n04 = en el centro del personaje (iluminación, clase 10)\n05 = alrededor de la referencia (1er efecto de clase 05), yendo hasta el oponente",
  "en": "POSITION (+0x0A)\n01 = static, spawned at the reference (like group 00)\n02 = around the character (auras)\n04 = at the character's center (lighting/shadow, class 10)\n05 = around the reference (1st class 05 effect), traveling to and chasing the opponent"
 },
 "h_bB": {
  "pt": "ESTADO (+0x0B) — hipótese\n04 = continua enquanto o estado estiver ativo (auras de carregamento, auras que ficam até usar especial).",
  "es": "ESTADO (+0x0B) — hipótesis\n04 = sigue mientras el estado esté activo.",
  "en": "STATE (+0x0B) — hypothesis\n04 = keeps going while the state is active."
 },
 "h_invoke": {
  "pt": "GRUPO DE INVOCAÇÃO (+0x08): o momento em que o mini-efeito aparece.\n00 = início/carregamento (só nessa etapa)\n01 = lançamento (só nele)\n02 = saídas de luz / fim\n03 = auras padrão (Final Flash, Electric Kamehameha…)\n04 = evento 'Vfx 5' (explosão no oponente)\n05 = complemento de iluminação (quase sempre classe 10)\nVeja 'Classes e grupos' para a explicação completa.",
  "es": "GRUPO DE INVOCACIÓN (+0x08): el momento en que aparece.\n00 = inicio/carga\n01 = lanzamiento\n02 = salidas de luz / final\n03 = auras estándar\n04 = evento 'Vfx 5' (explosión)\n05 = complemento de iluminación (clase 10)",
  "en": "INVOKE GROUP (+0x08): when the mini-effect appears.\n00 = start/charge\n01 = launch\n02 = light bursts / end\n03 = standard auras\n04 = 'Vfx 5' event (explosion)\n05 = lighting complement (class 10)"
 },
 "info_classes": {
  "pt": "CLASSES E GRUPOS (documentação Madeirada)\n\nCLASSE = o tipo do mini-efeito (a coluna 'Classe' da lista):\n• 00 — global: o primeiro mini-efeito de todo 03_.dat, as listras brancas. Não pode ser removido (só ocultado).\n• 02 — saídas/feixes de luz, típicas dos Kamehamehas. Cores RGBA em bytes nos offsets 0x0C, 0x1C e 0x2C de cada sessão de 120 bytes.\n• 05 — complementares em geral: faíscas, a esfera na ponta do feixe, o rastro de velocidade atrás do personagem, auras.\n• 09 — rodelas/efeitos que são lançados junto com o feixe ou projétil.\n• 0E — arquivos V00: efeitos BASE do carregamento (esferas, círculos). Têm formato, tamanho, rotação e posição próprios.\n• 10 — iluminação (e sombra) do personagem e do ataque.\n• 11 — caudas de feixes e de projéteis não redondos (Death Beam em barragem, Super Energy Wave Volley…).\n• 12 — raios em volta do personagem ou da esfera (Makankosappo).\n\nGRUPO = o momento e o jeito da invocação (é o que o programa chama de 'Fase'):\n• 00 — início/carregamento, só nessa etapa, em volta da referência (a referência do grupo 00 é sempre um V00).\n• 01 — lançamento, só no lançamento. A referência é o primeiro efeito da classe 05.\n• 02 — saídas de luz.\n• 03 — auras padrão (Final Flash, Electric Kamehameha, Kamehameha Solar…).\n• 04 — evento Vfx 5 (explosão).\n• 05 — complemento de iluminação, quase sempre na classe 10. (Correção: o grupo 05 NÃO é o que faz perseguir o oponente; isso é o byte +0x0A = 05.)\n\nOs bytes +0x09, +0x0A e +0x0B de cada mini-efeito completam o comportamento — veja os botões '?' na aba Tamanho e tempo.",
  "es": "CLASES Y GRUPOS (documentación Madeirada)\n\nCLASE = el tipo del mini efecto:\n• 00 — global: el primer mini efecto de todo 03_.dat, las rayas blancas. No se puede quitar (solo ocultar).\n• 02 — salidas/haces de luz (Kamehameha). RGBA en bytes en 0x0C, 0x1C y 0x2C de cada sesión de 120 bytes.\n• 05 — complementarios: chispas, esfera en la punta del rayo, rastro de velocidad, auras.\n• 09 — aros/efectos lanzados con el rayo o proyectil.\n• 0E — archivos V00: efectos BASE de la carga.\n• 10 — iluminación (y sombra).\n• 11 — colas de rayos y proyectiles no redondos.\n• 12 — rayos alrededor del personaje o de la esfera.\n\nGRUPO = momento y forma de invocación ('Fase' en el programa):\n• 00 — inicio/carga.\n• 01 — lanzamiento (referencia: 1er efecto de clase 05).\n• 02 — salidas de luz.\n• 03 — auras estándar.\n• 04 — evento Vfx 5 (explosión).\n• 05 — complemento de iluminación (clase 10). (Corrección: el grupo 05 NO hace perseguir al oponente; eso es el byte +0x0A = 05.)",
  "en": "CLASSES AND GROUPS (Madeirada docs)\n\nCLASS = the mini-effect type:\n• 00 — global: first mini-effect of every 03_.dat, the white stripes. Can't be removed (only hidden).\n• 02 — light bursts (Kamehameha). RGBA bytes at 0x0C, 0x1C, 0x2C of each 120-byte session.\n• 05 — general complements: sparks, sphere at the beam tip, speed trail, auras.\n• 09 — rings thrown with the beam/projectile.\n• 0E — V00 files: BASE charge effects.\n• 10 — lighting (and shadow).\n• 11 — tails of beams and non-round projectiles.\n• 12 — lightning around the character or sphere.\n\nGROUP = when/how it's invoked ('Phase' in the program):\n• 00 — start/charge.\n• 01 — launch (reference: 1st class 05 effect).\n• 02 — light bursts.\n• 03 — standard auras.\n• 04 — Vfx 5 event (explosion).\n• 05 — lighting complement (class 10). (Correction: group 05 does NOT chase the opponent; that's byte +0x0A = 05.)"
 },
 "tex_title": {
  "pt": "Texturas do efeito",
  "es": "Texturas del efecto",
  "en": "Effect textures"
 },
 "tex_info": {
  "pt": "Imagem",
  "es": "Imagen",
  "en": "Image"
 },
 "tex_used": {
  "pt": "Usos",
  "es": "Usos",
  "en": "Uses"
 },
 "tex_export": {
  "pt": "Exportar PNG…",
  "es": "Exportar PNG…",
  "en": "Export PNG…"
 },
 "tex_import": {
  "pt": "Importar PNG…",
  "es": "Importar PNG…",
  "en": "Import PNG…"
 },
 "tex_hide_dbt": {
  "pt": "Ocultar tudo que usa este DBT",
  "es": "Ocultar todo lo que usa este DBT",
  "en": "Hide everything using this DBT"
 },
 "tex_hide_q": {
  "pt": "Deixar invisíveis os {n} mini-efeitos que usam este DBT?",
  "es": "¿Hacer invisibles los {n} mini efectos que usan este DBT?",
  "en": "Make the {n} mini-effects using this DBT invisible?"
 },
 "tex_users": {
  "pt": "Mini-efeitos que usam esta imagem (posição e tamanhos editáveis):",
  "es": "Mini efectos que usan esta imagen (posición y tamaños editables):",
  "en": "Mini-effects using this image (position and sizes editable):"
 },
 "tex_nouser": {
  "pt": "Nenhum mini-efeito usa esta imagem diretamente (pode ser usada em sequência/animação).",
  "es": "Ningún mini efecto usa esta imagen directamente.",
  "en": "No mini-effect uses this image directly (it may be part of a sequence)."
 },
 "tex_imported": {
  "pt": "Textura importada: ajustada para a resolução e a quantidade de cores originais.",
  "es": "Textura importada: ajustada a la resolución y cantidad de colores originales.",
  "en": "Texture imported: fit to the original resolution and color count."
 },
 "hex_title": {
  "pt": "Editor hexadecimal",
  "es": "Editor hexadecimal",
  "en": "Hex editor"
 },
 "hex_known": {
  "pt": "Mostrar o que o programa sabe de cada byte",
  "es": "Mostrar lo que el programa sabe de cada byte",
  "en": "Show what the program knows about each byte"
 },
 "hex_meaning": {
  "pt": "Significado",
  "es": "Significado",
  "en": "Meaning"
 },
 "hex_unknown": {
  "pt": "Sem informação conhecida",
  "es": "Sin información conocida",
  "en": "No known information"
 },
 "hex_saved": {
  "pt": "Arquivo salvo.",
  "es": "Archivo guardado.",
  "en": "File saved."
 },
 "hex_invalid": {
  "pt": "A alteração deixou o efeito inválido e não foi aplicada:",
  "es": "El cambio dejó el efecto inválido y no se aplicó:",
  "en": "The change made the effect invalid and wasn't applied:"
 },
 "extras_trunks": {
  "pt": "Trunks Dome",
  "es": "Trunks Dome",
  "en": "Trunks Dome"
 },
 "kind_aura_trunks": {
  "pt": "Trunks Dome",
  "es": "Trunks Dome",
  "en": "Trunks Dome"
 }
})

T.update({"info_phases": {
 "pt": "O QUE SÃO AS FASES (GRUPOS DE INVOCAÇÃO)\n\nCada mini-efeito tem um grupo de invocação (byte +0x08) que diz EM QUE MOMENTO ele aparece. O programa usa esse valor para montar os grupos iniciais ('Fase N').\n\n• Fase/grupo 00 → início/carregamento\n• 01 → lançamento\n• 02 → saídas de luz / fim\n• 03 → auras padrão\n• 04 → evento Vfx 5 (explosão no oponente)\n• 05 → complemento de iluminação (classe 10)\n\nAo combinar: o mini-efeito importado continua no grupo dele. Se a animação do personagem de destino não liga aquele evento, ele não aparece; por isso existe 'Fase dos importados'.\n\nPara a explicação completa de classes e grupos, use o botão 'ⓘ Classes e grupos' no topo.",
 "es": "QUÉ SON LAS FASES (GRUPOS DE INVOCACIÓN)\n\nCada mini efecto tiene un grupo (byte +0x08) que indica EN QUÉ MOMENTO aparece.\n\n• 00 → inicio/carga\n• 01 → lanzamiento\n• 02 → salidas de luz / final\n• 03 → auras estándar\n• 04 → evento Vfx 5 (explosión)\n• 05 → complemento de iluminación (clase 10)\n\nVer 'ⓘ Clases y grupos' arriba para la explicación completa.",
 "en": "WHAT PHASES ARE (INVOKE GROUPS)\n\nEach mini-effect has an invoke group (byte +0x08) saying WHEN it appears.\n\n• 00 → start/charge\n• 01 → launch\n• 02 → light bursts / end\n• 03 → standard auras\n• 04 → Vfx 5 event (explosion)\n• 05 → lighting complement (class 10)\n\nSee 'ⓘ Classes and groups' at the top for the full explanation."}})

T.update({
 "about_text": {
  "pt": "Effects Max Ultra Legendary Studios v1.1\nEditor de efeitos de Budokai Tenkaichi 3.\n\nCréditos:\nClaude IA (programação, interface)\nAriel Sofia (testes, elaboração, aplicação e execução)\nMadeirada BR (documentação e programa de Shaders usado de base no código)\nLegendary (documentação, ideias, soluções e afins)\nMaxBound Studios\n\nVivethemodder (documentação)\nVras (documentação)\nHunter (alguns dos efeitos usados de base para a criação)\nHiro Tex\nTeam BT4",
  "es": "Effects Max Ultra Legendary Studios v1.1\nEditor de efectos de Budokai Tenkaichi 3.\n\nCréditos:\nClaude IA (programación, interface)\nAriel Sofia (pruebas, elaboración, aplicación y ejecución)\nMadeirada BR (documentación y programa de Shaders usado como base)\nLegendary (documentación, ideas, soluciones y más)\nMaxBound Studios\n\nVivethemodder (documentación)\nVras (documentación)\nHunter (algunos efectos usados como base)\nHiro Tex\nTeam BT4",
  "en": "Effects Max Ultra Legendary Studios v1.1\nBudokai Tenkaichi 3 effect editor.\n\nCredits:\nClaude IA (programming, interface)\nAriel Sofia (testing, design, application and execution)\nMadeirada BR (documentation and the Shader program used as a code base)\nLegendary (documentation, ideas, solutions and more)\nMaxBound Studios\n\nVivethemodder (documentation)\nVras (documentation)\nHunter (some effects used as a base)\nHiro Tex\nTeam BT4"
 },
 "dark_mode": {
  "pt": "Modo noturno",
  "es": "Modo nocturno",
  "en": "Dark mode"
 },
 "dark_restart": {
  "pt": "O modo noturno foi desligado. Algumas cores só voltam ao normal depois de reabrir o programa.",
  "es": "El modo nocturno se desactivó. Algunos colores vuelven a la normalidad al reabrir el programa.",
  "en": "Dark mode turned off. Some colors return to normal after reopening the program."
 },
 "no_image": {
  "pt": "Ainda não há imagem ilustrativa para este item.",
  "es": "Aún no hay imagen ilustrativa para este elemento.",
  "en": "No illustrative image for this item yet."
 },
 "ch_red": {
  "pt": "Vermelho",
  "es": "Rojo",
  "en": "Red"
 },
 "ch_green": {
  "pt": "Verde",
  "es": "Verde",
  "en": "Green"
 },
 "ch_blue": {
  "pt": "Azul",
  "es": "Azul",
  "en": "Blue"
 },
 "ch_int": {
  "pt": "Intensidade",
  "es": "Intensidad",
  "en": "Intensity"
 },
 "ch_color1": {
  "pt": "Cor 1:",
  "es": "Color 1:",
  "en": "Color 1:"
 },
 "ch_color2": {
  "pt": "Cor 2:",
  "es": "Color 2:",
  "en": "Color 2:"
 },
 "info_channels": {
  "pt": "INVERTER E COPIAR (como no Skill Shader Editor)\n\n• Inverter: troca os valores da Cor 1 com os da Cor 2 em todas as linhas (ex.: Vermelho ↔ Azul transforma um efeito vermelho em azul mantendo os tons).\n• Copiar: copia a Cor 1 para a Cor 2 em todas as linhas.\n\nOs valores mudam nas caixas; clique em Aplicar para gravar.",
  "es": "INVERTIR Y COPIAR (como en el Skill Shader Editor)\n\n• Invertir: intercambia Color 1 y Color 2 en todas las filas.\n• Copiar: copia Color 1 a Color 2 en todas las filas.\n\nLos valores cambian en las casillas; haz clic en Aplicar para guardar.",
  "en": "SWAP AND COPY (like the Skill Shader Editor)\n\n• Swap: exchanges Color 1 and Color 2 in all rows.\n• Copy: copies Color 1 into Color 2 in all rows.\n\nValues change in the boxes; click Apply to write them."
 },
 "tex_recolor": {
  "pt": "Mudar cor…",
  "es": "Cambiar color…",
  "en": "Change color…"
 },
 "needs_beam": {
  "pt": "(só em golpes com feixe)",
  "es": "(solo en ataques con rayo)",
  "en": "(beam moves only)"
 },
 "kind_aura_ff": {
  "pt": "Final Flash Blue",
  "es": "Final Flash Blue",
  "en": "Final Flash Blue"
 },
 "kind_aura_ff2": {
  "pt": "Final Flash",
  "es": "Final Flash",
  "en": "Final Flash"
 },
 "kind_ffk_rings": {
  "pt": "Rodelas (Full Force Kamehameha)",
  "es": "Aros (Full Force Kamehameha)",
  "en": "Rings (Full Force Kamehameha)"
 },
 "kind_paikuhan_rings": {
  "pt": "Rodelas (Madam Paikuhan)",
  "es": "Aros (Madam Paikuhan)",
  "en": "Rings (Paikuhan Madam)"
 }
})
