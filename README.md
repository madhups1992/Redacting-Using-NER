# cs5293sp19-project1

# cs5293sp19-project0
Madhumitha Pachapalayam Sivasalapathy

Run the code :

        "pipenv run python -m pytest" is used to test all the test cases.(writen some random text to test each fields)
        "pipenv run python project1/main.py --input '*.txt' --date --name --phone --address --geneders --concept 'kids'  --output 'others'  --stats 'stasfile'" is used to run project0 and can run our modules
	"cat project1/stasfile.txt " will show the statistics of redacted files and the details of every fields	

Please refer the saved files in the following location :

        statistics of .txt files is stored in \project\*1\project1\stasfile.txt .

Modules:
        Created the following module
	
	1.Reading the files from Directory: It reads all the files with from the same directory and the files from other direcotory
	
	2.Extracting Date(Analized most of the examples and constructed regexp), name(Used Nltk person to extract), phone(Analized most of the way of representation), concept(compared the similar meaning sentence and extracted), and addresss(compared most common format and created a regex to extract the address)

	3.Redation : Redated the data that contains the things needed for redation which are extracted from each modules of date, name, phone, address, genders, concepts.

	4.Storage : The redacted files are stored in the location same location

	5.Statistics : Counts of each modules of each file are calculated and stored in the same location    



Test cases: Unit testing is done for every module

        * Test case 1: To check all files are fetched from same folder and other folder. 
        * Test case 2: To check whether unit is extacting all the address with different formats.
        * Test case 3: Different date formats are extracted properly. 
        * Test case 4: All the gender is extracted properly.
        * Test case 5: Name is extracted properly.
	* Test case 6: Concept with similar concepts are extracted properly.
	* Test case 7: Phone number with differnt formats are extracted and redacted.


Reference:

        "https://docs.python.org" - Used the website for python usage.
        Used assignment0's test modules to construct testcases.



