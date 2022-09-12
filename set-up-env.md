# How to set up python virtual environment


# What are virtual environments and why should I them?
As you go along your programming journey, you will find to learn that various projects require different versions of the same python libraries. You will learn that many different version of those libraries require another library as a requirement for them to work and they also need to be a specific version. Managing this in the global python envirement is bad practice and will lead to conflicts down the line, a term usually coined as "dependency hell". Virtual environments are a way to mediate this, by isolating each project in a seperate python environment. This way, you can have different versions of the these libraries.

# How to set up a virtual environment

Python versions 3.3 and above come with a built in module called venv. This module allows you to create a virtual environment. To create a virtual environment, you need to create a folder and then run the following command in the terminal:

    python/python3 -m venv <name of virtual environment>

this will create a folder with the name of the virtual environment you specified. To activate the virtual environment, you need to run the following command:

| Posix   | bash/zsh   | python venv/bin/activate     |
|---------|------------|------------------------------|
|         | csh/tcsh   | python venv/bin/activate.csh |
| Windows | cmd.exe    | venv\Scripts\activate.bat    |
|         | PowerShell | venv\Scripts\Activate.ps1    |


# How to tell your if your virtual environment is active

You can verify that your virtual environment is active by checking your terminal prompt. If you see the name of your virtual environment in parenthesis, then it is active. If you don't see it, then it is not active.
For example:

    (venv) USER@computer:~$
    (venv) C:\Users\USER\workspace\project>
You can also check if your virtual environment is active by running the following command:

    pip list

or 
    
    pip freeze

# How to deactivate your virtual environment

To deactivate your virtual environment, you need to run the following command:

    deactivate