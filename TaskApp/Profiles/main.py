from .models import Profile
from .Compare import Compare
import os

os.system('cls')
print("\n\n*Create instances of Profiles like the following examples. NOTE: if value doesn't exits then enter 'None' *")
print("a = Profile(first_name='Manoj', last_name='Kumar', email='manu1+donotcompare@g.com', class_year='2012',date_of_birth='2022-02-02')")
print("b = Profile(first_name='Mani', last_name='Kim', email='manu@g.com', class_year='2012',date_of_birth='2022-02-02')")
print("*Run find_duplicates() like this: *")
print("Dupe.find_duplicates(profiles=[a,b], fields=['email','first_name','last_name','class_year','date_of_birth'])")
class Dupe:
    def find_duplicates(profiles,fields):
        result = {'first_name': '', 'last_name': '', 'email': '', 'class_year': '', 'date_of_birth': ''}
        fields_copy = fields.copy()
        flags= ""
        matching_fields = []
        non_matching = []
        i=0
        while i < len(fields):
            if(fields[i]=='first_name'):
                    result.update(first_name = Compare.compare_fields(profiles[0].first_name, profiles[1].first_name))
                    flags = flags+'F'
                    fields_copy.pop(fields_copy.index('first_name'))
            elif(fields[i]=='last_name'):
                    result.update(last_name = Compare.compare_fields(profiles[0].last_name, profiles[1].last_name))
                    flags = flags + 'L'
                    fields_copy.pop(fields_copy.index('last_name'))
            elif(fields[i]=='email'):
                    result.update(email = Compare.compare_fields(profiles[0].email,profiles[1].email))
                    flags= flags + 'E'
                    fields_copy.pop(fields_copy.index('email'))
            elif(fields[i]=='class_year'):
                if((profiles[0].class_year != '' and profiles[0].class_year != 'None') and (profiles[1].class_year != '' and profiles[1].class_year != 'None')):
                    result.update(class_year=Compare.compare_fields(profiles[0].class_year,profiles[1].class_year))     
            elif(fields[i]=='date_of_birth'):
                if((profiles[0].date_of_birth != '' and profiles[0].date_of_birth != 'None') and (profiles[1].date_of_birth != '' and profiles[1].date_of_birth != 'None')):
                    result.update(date_of_birth = Compare.compare_fields(profiles[0].date_of_birth,profiles[1].date_of_birth))
            i= i + 1

        final_score, matching_fields, non_matching = Compare.calc_score(result, fields_copy , flags)
        skipped_values = []
        for key,value in result.items():
            if(value == ''):
                skipped_values.append(key)
        print(result)
        print("\nProfile 1, Profile 2, total match score : ", final_score, "\nMatching attributes: ", matching_fields)
        print("Non-matching attributes: ", non_matching)
        print("Ignored attributes: ", skipped_values)