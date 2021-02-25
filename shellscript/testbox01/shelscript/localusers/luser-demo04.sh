#!/bin/bash


# This script creates an account on the local system.
# You will be prompted for the account name and password.

# Ask for user name.
read -p 'Enter the username to create: ' USER_NAME

# Ask for real name.
read -p 'Enter the name of the person who this account is for: ' COMMENT

# Ask for password.
read -p 'Enter the password to use for hte account: ' PASSWORD

# Create the usr.
useradd -c "${COMMENT}" -m ${USER_NAME}

# Set the password for the user.
echo ${PASSWORD} | passwd --stdin ${USER_NAME}
# Force password change on first login.
passwd -e ${USER_NAME}
