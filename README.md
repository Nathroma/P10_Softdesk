#SoftDesk

Cette API Rest est concue afin d'assurer un suivi de problèmes sur plusieurs platformes

Documentation de l'API : (https://documenter.getpostman.com/view/17390561/UVRDEk4o).

<h2>Utilisation</h2>

Récupérez l'ensemble du projet :

`git clone https://github.com/Nathroma/P10_Softdesk`

Pour pouvoir lancer le programme, créez un environnement virtuel :

`python -m venv env`

Activez l'environnement :

`env/Scripts/activate (sous windows)`

Installez les packages requis à l'aide de la commande suivante :

`pip install -r requirements.txt`

Faire les migrations si nécéssaire :

`softdesk\manage.py makemigrations`
`softdesk\manage.py migrate`

Puis lancez le serveur en utilisant la commande:

`python .\softdesk\manage.py runserver`

Pour finir utilisez Postman (de préférence) pour utiliser l'API

Lien local pour utilisation avec navigateur web : http://127.0.0.1:8000/