from pyscript import document, display

members = ['Shari Cruz', 'Tiana Bayou', 'Nani Pelekai', 'Cookie Monster', 'Colette Tatou']

def new_members(e):
    document.getElementById('new_members').innerHTML = " " #clears previous result
    f_name = document.getElementById('fname').value
    l_name = document.getElementById('lname').value

    full_name = f_name + " " + l_name


    # sets of club members
    gr7 = {'Lilo Pelekai', 'Russell Grayson'}
    gr8 = {'Riley Anderson', 'Meilin Lee'}
    gr9 = {'Wendy Darling', 'Andy Davis'}
    gr10 = {'Shari Cruz', 'Mirabel Madrigal'}

    #combines all sets into one
    all_members = gr7 | gr8 | gr9 | gr10

    members_list = "<br>".join(sorted(all_members))

    #counts how many names there are on a list

    display(f"Welcome Members! :")
    display(f"Total Members in the Club: {len(all_members)}", target="new_members")










 







   


  