from pyscript import display, document # type: ignore


def customer_form(e):
    item1 = document.getElementById("champ")
    item2 = document.getElementById("mousse")
    item3 = document.getElementById("entre")
    item4 = document.getElementById("coq")
    item5 = document.getElementById("rat")
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number").value
    total = (float(item1.value) * float(item1.checked) + 
             float(item2.value) * float(item2.checked) + 
             float(item3.value) * float(item3.checked) +
             float(item4.value) * float(item4.checked) +
             float(item5.value) * float(item5.checked))
    
    display(f'Order for: {name}')
    display(f'Address: {address}')
    display(f'Contact number: {number}')
    display(f'Total amount: {total:.2f}€')