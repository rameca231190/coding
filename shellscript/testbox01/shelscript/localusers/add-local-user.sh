#!/bin/bash
# This script creates new user in a local system.
# You must supply username as an argument to the script.
# Optionaly, you can also provide a comment for the account as an argument.
# Password will be automatically generated.
# Display UID and username of the user executing this script.
# Display if the user is the root user or not.

# Display the UID.
echo "Your UID is ${UID}"

# Display if the UID does NOT match 0.
if [[ "$UID" -ne 0 ]]
then
  echo "Please run with sudo or as root."
  exit 1
fi
# If they don't supply at least one argument, then give them help.
if [[ "${#}" -lt 1 ]]
then
  echo "Usage: ${0} USER_NAME [COMMENT]..."
  echo 'Create an account on the local system with the name of USER_NAME and a comments field of COMMENT'
  exit 1
fi

# The first parameter is the user name 1 is position.
USER_NAME="${1}"

# The rest of the parameters are for the account comments.
shift 
COMMENT="${@}"

# Generate a password.
PASSWORD="$(date +%s%N | sha256sum | head -c48)"

# Create the user with the password.
useradd -c "${COMMENT}" -m ${USER_NAME}

# Check to see if the useradd comand succeded.
# We don't want to tell the user that an account was created when it hasn't been.
if [[ "${?}" -ne 0 ]]
then
  echo 'The account could not be created.'
  exit 1
fi

# Set the password.
echo ${PASSWORD} | passwd --stdin ${USER_NAME}

# Check to see id the password command succeded.
if [[ "${?}" -ne 0 ]]
then
  echo 'The password for the account could not be set.'
  exit 1
fi

# Force password change on first login.
passwd -e ${USER_NAME}

# Display the username, password, and the host where the user was created.
echo 
echo "The username created is: ${USER_NAME}"
echo
echo "The password for: ${USER_NAME} is: ${PASSWORD}"
echo
echo "host: ${HOSTNAME}"
exit 0
