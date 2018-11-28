import csv

#  We need to sort players into two lists.
experienced = []
noExperience= []


LETTER = '''Hello {},
We are excited to inform you that, {} has 
been chosen to play for the {}! Please arrive
for practice at 9:30am next Saturday!
'''


def read_and_sort():
    
    #opens the soccer players CSV file that was given to us.

    with open("soccer_players.csv", newline = "") as csv_data:
        playerreader = csv.reader(csv_data)
        rows = list(playerreader)
        del(rows[0])
        
        #I added the next function to remove duplicated data.
        #next(playerreader)
    #create a function to look for YES and add players to lists based on experience.
        
        for word in rows:
          if word[2] == "YES":
            experienced.append(word)
          else:
            noExperience.append(word)

        
def new_file():        
        #Write the new file 
        with open("teams.txt", "w") as new_file:
            
          #In the teams.txt file seperate the three lines of players info.
            dragons = experienced[:3] + noExperience[:3]
            sharks = experienced[3:6] + noExperience[3:6]
            raptors = experienced[6:] + noExperience[6:]

            #  Categorize the team slices to three distinct groups.
            the_teams = {"Dragons": dragons, "Sharks": sharks, "Raptors": raptors}
                     

            #Use of 'the_teams' to begin writing text files, this will write team names
            
            for name, team in the_teams.items():               
                new_file.write("\n{}\n".format(name))
                
                #The ROSTER
                for position in team:
                    new_file.write("{}, {}, {}\n".format(position[0], position[2], position[3]))
                    
                    #The message setup that I will use to write the letter to player guardians.
                    message = position[0]
                    with open(message, 'w') as letter_for_guardians:
                       letter_for_guardians.write(LETTER.format(position[-1], position[0], name))
                    
                        
# the dunder main starts the program. All functions are entered inside the if block.
if __name__ == '__main__':
    read_and_sort()
    new_file()
