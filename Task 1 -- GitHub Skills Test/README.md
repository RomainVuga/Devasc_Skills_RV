Task 1 -- Github Skills Test


Preparation: 
Open the Devasc VM, log into Github and have your Github Token ready.


Implementation:
Step 1: Create a repository on Github named “Devasc_Skills_RV”
Created a public repository

Step 2: Clone the repository on the VM.
-> git clone https://github.com/RomainVuga/Devasc_Skills_RV.git

Step 2: Use your token to link the local git repo with the repo online.
-> cd Devasc_Skills_RV
-> git remote set-url origin https://MyToken@github.com/RomainVuga/Devasc_Skills_RV.git


Troubleshooting: 
When trying to run “git remote set-url…” is forgot to first move into the repo in my terminal on the VM by using cd.


Verification: 
Can i push new files to my online repo?
