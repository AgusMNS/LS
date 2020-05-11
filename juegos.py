import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg

def datosCompleto(valores, evento): #funcion corroboro que esten todos los datos
	aceptar=True
	for valor in valores: 
		if(valores[valor]==''):
			aceptar=False
	return aceptar
	
def jugadoresJuegos(valores, evento, window,j):  #agrego un usuario con una lista vacia de juegos a la que se le va a agregar cuando seleccione el juego.
	seguir='No'
	while(seguir=='No'):
		if valores['usuario'] not in j.keys(): #Si el usuario no esta registrado
			seguir='Yes'
			aceptar=False
			while not evento in (None, 'Cancel') and (aceptar==False):  #corroboro que no falten datos
				aceptar=datosCompleto(valores, evento)
				if(aceptar==False):
					sg.popup('No ha ingresado todos los datos, por favor vuelva a intentarlo')
					evento, valores=window.read()   #si faltan, entonces los vuelvo a ingresar
			if(aceptar):   							#si estan todos los datos, los guardo en el diccionario
				j[valores['usuario']]=[{'edad':valores['edad'],'email':valores['email'],'contrasena':valores['contra']}, list()]
		else:
			seguir=sg.popup_yes_no('Ese usuario ya esta registrado, desea jugar con los datos de ese usuario? De lo contrario debe volver a registrarse') 
			if(seguir=='No'):
				evento, valores=window.read()
		if(evento=='Cancel'):
			return False

def main(args):
	with open('jugadores.txt','a+') as archivo: #lo abro en modo append ya que en caso de no existir el archivo, crea uno nuevo y no da error, y si existe, puedo agregar nuevos jugadores. 
		if(archivo.tell()>0):   #Me fijo si el archivo esta vacio, si ya se registraron usuarios entonces tengo que agregar al diccionario ya creado
			archivo.seek(0)     #voy al inicio del archivo para poder tomar los datos
			jugadores=json.load(archivo)
		else:
			jugadores=dict()      #Si todavia no hubo jugadores entonces creo el diccionario
		sigo_jugando = True
		window = sg.Window('Menu de Juegos', layoutMenu)
		event, values = window.read()
		while sigo_jugando:
			if not event in (None, 'Cancel'):
				if(jugadoresJuegos(values, event, window, jugadores)==False): #Si no toque cancelar cuando agregaba usauarios, lo proceso
					sigo_jugando=False
				else:                 
					if values['juego'] == ['Ahorcado']:
						hangman.main()
						jugadores[values['usuario']][1].append('ahorcado')  #agrego a la lista de juegos, el nuevo juego seleccionado
					elif values['juego'] == ['Ta-TE-TI']:
						tictactoeModificado.main()
						jugadores[values['usuario']][1].append('TA-TE-TI')
					elif values['juego'] == ['Otello']:
						reversegam.main()
						jugadores[values['usuario']][1].append('otello')
					print('Termino el juego! Vuelva a la pantalla de Menu de Juegos')
					event, values = window.read()
			else:
				sigo_jugando = False
		window.close()
	with open('jugadores.txt', 'w') as archivo:  #sobrescribo el archivo con los datos actualizados
		json.dump(jugadores, archivo)

sg.theme('LightGreen4')
juegos = ('Ahorcado', 'Ta-TE-TI', 'Otello')
layoutMenu= [
		[sg.Text('Menu de Juegos', size=(15, 1),justification='center', font=("Fixedsys", 25))],
		[sg.Text('-Por favor ingrese sus datos: ',justification='center',font=('Fixedsys'))],
		[sg.Text('Usuario: ', font=('Fixedsys'),justification='center'), sg.Input(key='usuario')],
		[sg.Text('Edad: ', font=('Fixedsys')), sg.Input( key='edad')],
		[sg.Text('Email: ', font=('Fixedsys')), sg.Input( key='email')],
		[sg.Text('Contrasena: ', font=('Fixedsys')), sg.Input( key='contra')],
		[sg.Text('-Si ya tiene su usuario ingresado puede seleccionar\nun juego y continuar!',font=('Fixedsys'))],
		[sg.Listbox(juegos, size=(15, len(juegos)), key='juego')],
		[sg.Submit(), sg.Cancel()]
			]

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
