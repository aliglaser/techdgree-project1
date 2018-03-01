import csv
import random


players=[]
team1=[]
team2=[]
team3=[]
rows = []

def read_file():
	with open('soccer_players.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			players.append(line['Name'])


	team1 = random.sample(players, 6)
	for member in team1:
		players.remove(member)
	team2 = random.sample(players, 6)
	for member in team2:
		players.remove(member)
	team3 = players
	print("tea1: {}\nteam2: {}\nteam3:{}:".format(team1, team2, team3))		

	
	
	with open('players.csv', 'w') as csvfile:
		fieldnames = ['Name', 'Soccer Experience', 'Guardian Name(s)']
		playerWriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
		playerWriter.writeheader()
		for member in team1:
			for row in rows:
					if row['Name'] == member:
						playerWriter.writerow({
								'Name':member,
								'Soccer Experience':row['Soccer Experience'],
								'Guardian Name(s)':row['Guardian Name(s)']
							})
		for member in team2:
			for row in rows:
					if row['Name'] == member:
						playerWriter.writerow({
								'Name':member,
								'Soccer Experience':row['Soccer Experience'],
								'Guardian Name(s)':row['Guardian Name(s)']
							})
		for member in team3:
			for row in rows:
					if row['Name'] == member:
						playerWriter.writerow({
								'Name':member,
								'Soccer Experience':row['Soccer Experience'],
								'Guardian Name(s)':row['Guardian Name(s)']
							})												




def read_players():
	for person in players:
		print(person)			





	



if __name__ == "__main__":
	read_file()