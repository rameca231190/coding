#!/bin/bash
# This script creates new user in a local system.

# Display UID and username of the user executing this script.
# Display if the user is the root user or not.


# Display the UID.
echo "Your UID is ${UID}"

# Display if the UID does NOT match 0.
UID_TO_TEST_FOR='0'
if [[ "$UID" -ne ${UID_TO_TEST_FOR} ]]
then
  echo "Please run with sudo or as root."
  exit 1
fi

# Display the username.
USER_NAME=$(id -un)

# Ask for user name.
read -p 'Enter the username to create: ' USER_NAME

# Ask for real name.
read -p 'Enter the name of the person who this account is for: ' COMMENT

# Ask for password.
read -p 'Enter the password to use for hte account: ' PASSWORD

# Create the user.
useradd -c "${COMMENT}" -m ${USER_NAME}

# Test if the command succeeded.
if [[ "${?}" -ne 0 ]]
then
  echo 'The account could not be created.'
  exit 1
fi

# Set the password for the user.
echo ${PASSWORD} | passwd --stdin ${USER_NAME}
# Force password change on first login.
passwd -e ${USER_NAME}

# Test if the command succeeded.
if [[ "${?}" -ne 0 ]]
then
  echo 'The password for the user cannot be created.'
  exit 1
fi

# Display the username and password created.
echo 
echo "The username created is: ${USER_NAME}"
echo
echo "The password for: ${USER_NAME} is: ${PASSWORD}"

echo "host: ${HOSTNAME}"
exit 0
