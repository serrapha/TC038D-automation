This is a simple automation for the TC-038D oven, designed to make step-wise safe changes in the temperature of a crystal. 

# How to install it 
The automation was made under a Python virtual environment containing the instrumentkit library and a Numpy downgraded to version 1.26.0. So, consider pip installing the requirements file or manually verifying your versions. 

# How to use it 
1. Connect the serial channel with the command ```hcp.TC038D.open_serial('COMX')``` where X is your channel number. To check it on Windows, use ```Win + R``` followed by ```devmgmt.msc```. The channel will be labeled under 'COM'. 
2. When running the script, it will ask for your target temperature, your step, and the wait time. The step will simply add to your current temperature until the target temperature is reached and it will wait the desired time. 

# Issues
For any issues with the script, please write to me on GitHub. 
