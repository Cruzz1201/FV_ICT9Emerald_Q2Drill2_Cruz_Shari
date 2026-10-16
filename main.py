from pyscript import document, display

gr7 = {'Lilo Pelekai', 'Russell Grayson', 'Vennelope Von Schweetz', 'Elio Solis'}
gr8 = {'Riley Anderson', 'Meilin Lee', 'Luca Paguro', 'Miguel Rivera'}
gr9 = {'Wendy Darling', 'Andy Davis', 'Barley Lightfoot'}
gr10 = {'Shari Cruz', 'Mirabel Madrigal', 'Kida Tatch'}

all_verified_members = gr7.union(gr8, gr9, gr10) #combines all the sets into one master list. 

def new_members(e):
    document.getElementById('new_members').innerHTML = " " #clears previous result
    f_name = document.getElementById('fname').value.strip()
    l_name = document.getElementById('lname').value.strip()

    added_person = f_name + " " + l_name
    real_members = all_verified_members | {added_person}

    true_members = "<br>".join(sorted(real_members))

    # display(f"<b>Welcome HE Club Members!:</b><br>{real_members}", target="new_members")
    # display(f"<br>Total Members in the Club: {len(real_members)}", target="new_members") #counts how many names there are on a list

    document.getElementById('new_members').innerHTML = (
        f"<b><i>Official HE Club Members:</i></b><br> {true_members}<br><br> Total Members in the Club: {len(real_members)}"
    )
