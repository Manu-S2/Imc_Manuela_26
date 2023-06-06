import PySimpleGUI as sg

sg.theme("SystemDefaultForReal")

layout=[
  
  [sg.Push(),sg.Text('Índice de massa corpórea'),sg.Push()],
  [sg.Push(),sg.Text('Massa:'),sg.Input(key='-MASS-',size=(40,1)),sg.Push()],
  [sg.Push(),sg.Text('Altura:'),sg.Input(key='-HIGH-',size=(40,1)),sg.Push()],
  [sg.Push(),sg.Button('Calcular'),sg.Push()]
  
  ]
  
window = sg.Window('IMC',layout = layout, font= 'Monaco 18')

while True:
  event,value = window.read()
  print(event,value)
  massa = float(value['-MASS-'])
  altura = float(value['-HIGH-'])
  imc = massa/(altura**2)
  sg.Popup(f'Seu IMC é {imc:.2f}', font= '26')
  if event =='QUIT' or event == sg.WIN_CLOSED:
    Break
