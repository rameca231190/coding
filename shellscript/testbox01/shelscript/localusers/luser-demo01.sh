#!/bin/bash

#This script displays various information to the screen.
#Display hello
echo 'Hello World'

# Assign a value to a variable 
WORD='script'

# Display that value using the variable (Use doblequotes with variables).
echo "$WORD"


# Demonstrate that sinfle quotes cause variables to NOT get expanded.
echo '$WORD'

# combine the variable with hard-coded text.
echo "This is a shell $WORD"

#Display contets of the vatiable using an alternative syntax.
echo "This is a shell ${WORD}"

# Append text to the vatiable.
echo "${WORD}ing is fin!"

# Show how NOT to append text to a variable.
# This doesn't work:
echo "$WORDing is fun!"

# Create a new variable

ENDING='ed'

# Combine the 2 variables.

echo "This is ${WORD}${ENDING}."


# Change the value stored in the ENDING variable. (Reassignment.)
ENDING='ing'
echo "${WORD}${ENDING} is fun!"

# Reasign value to ENDING.
ENDING='s'
echo "You are going to write many ${WORD}${ENDING} in this class!"