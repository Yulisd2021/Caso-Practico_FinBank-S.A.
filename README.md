# Caso-Practico_FinBank-S.A.
ESCENARIO A  BANCA DE SERVICIOS FINANCIEROS.
Este repositorio se crea con el objetivo de realizar prueba técnica para Ingeniero de datos -DataKnow
-	Para la realización del caso utilice las siguientes herramientas:
-	Plataforma: Azure Microsoft.
-	Herramienta IaC :
-GitHub Repositorio.GitHub
-Pyhton 3.12
-Visual Studio Code.
-SQL Server Management Studio
  Draw.io
          
-	Se creó la cuenta gratuita  de Azure  Microsoft.
  Se inició con la creación de la base de datos en el programa  SQL Server Management Studio
Creación de tablas y modelo entidad relación.

<img width="921" height="409" alt="image" src="https://github.com/user-attachments/assets/45805c9b-13f4-4792-bc7a-4618f47ee2b9" />

<img width="539" height="785" alt="image" src="https://github.com/user-attachments/assets/f078d2f8-2e3b-4ea5-b279-9fd895aa15f2" />


DIAGRAMA ENTIDAD RELACION.

<img width="967" height="558" alt="image" src="https://github.com/user-attachments/assets/6ad5a3ad-5317-482c-aaa3-6859fbf17f66" />


Recurso	Tipo	Función
casoFinBank	Azure Data Factory	-Donde  están los pipeline 
datoscaso1-	Cuenta de almacenamiento (Storage Account)	Contiene el archivo los archivos cvs 
FinBank S.A	Azure SQL Database	Base de datos
caso1	SQL Server	Servidor que aloja  la base de datos FinBank S.A.
FinBank	Grupo de recursos	Contenedor de todos los recursos.

Se debe realizar la conexión del servidor, Aquí al darle inicio nos sale la información del nombre del servidor creado

<img width="921" height="484" alt="image" src="https://github.com/user-attachments/assets/76c67419-5940-4e8b-a9ce-ab1ae71e7139" />




Se realiza la conexión de la base de datos en SQL Server Management y Azure

 <img width="921" height="445" alt="image" src="https://github.com/user-attachments/assets/847cd2c7-548c-45b8-9490-b28ddf618672" />

 

Se crea el Storage Account.    En este caso le coloque el nombre de datos caso1

<img width="579" height="593" alt="image" src="https://github.com/user-attachments/assets/5638f124-0468-4afe-9dd9-d46c4e7f5c79" />





Luego una vez se haya creado los archivos de CVS  en el cual se encuentran los datos sintéticos se procede a realizar el cargue de estos 


<img width="921" height="419" alt="image" src="https://github.com/user-attachments/assets/e9ee1ba9-620e-489b-aca5-94e83f5a1872" />



 
Una vez creado  en este caso se llama datos   accedemos 
 
Y buscamos los archivos cvs que se adjuntaran.
<img width="1002" height="453" alt="image" src="https://github.com/user-attachments/assets/5756b851-90df-403a-9982-5fba7393a22a" />

 
Archivos cvs cargados satisfactoriamente

<img width="921" height="435" alt="image" src="https://github.com/user-attachments/assets/217c2473-d795-4828-8804-36e2e689ad81" />


<img width="921" height="410" alt="image" src="https://github.com/user-attachments/assets/7c61e9ff-8a1d-43ce-9552-57f264e4fd49" />


 
Una vez creados se procede a  Azure Data Factory


CREANDO EL DATASET.

<img width="1909" height="963" alt="image" src="https://github.com/user-attachments/assets/26f1d0f7-2e4a-4f4b-8ed1-6f039efbd54b" />







