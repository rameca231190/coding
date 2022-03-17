import os
import subprocess
import sys
# Import run form subprocess to run linux commands
from subprocess import run

# Set up variable for Rancher env.
RANCHER_ENV = (f"{sys.argv[1]}")


# Pull the list of rancher clusters based on rancher_env condition.

if RANCHER_ENV == "sbx":
    cluster_name = subprocess.Popen("rancher clusters list | awk {'print $3'} | grep -i carbon-gcp ; rancher clusters list | awk {'print $4'} | grep -i carbon-gcp", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    cluster_name = cluster_name.replace("\n", " ")
    cluster_name = list(cluster_name.split(" "))
    print("The list of the clusters is: ", cluster_name)

elif RANCHER_ENV == "pre-dev":
    cluster_name = subprocess.Popen("rancher clusters list | awk {'print $3'} | grep -i 6335-carbon-stores ; rancher clusters list | awk {'print $4'} | grep -i 6335-carbon-stores", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    cluster_name = cluster_name.replace("\n", " ")
    cluster_name = list(cluster_name.split(" "))
    print("The list of the clusters is: ", cluster_name)

elif RANCHER_ENV == "dev":
    cluster_name = subprocess.Popen("rancher clusters list | awk {'print $3'} | grep -i 6332-carbon-stores ; rancher clusters list | awk {'print $4'} | grep -i 6332-carbon-stores; rancher clusters list | awk {'print $3'} | grep -i 6338-carbon-stores ; rancher clusters list | awk {'print $4'} | grep -i 6338-carbon-stores", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    cluster_name = cluster_name.replace("\n", " ")
    cluster_name = list(cluster_name.split(" "))
    print("The list of the clusters is: ", cluster_name)

elif RANCHER_ENV == "rona":
    cluster_name = subprocess.Popen("rancher clusters list | awk {'print $3'} | grep -i carbon-rona ; rancher clusters list | awk {'print $4'} | grep -i carbon-rona ; rancher clusters list | awk {'print $3'} | grep -i 6390-carbon-stores ; rancher clusters list | awk {'print $4'} | grep -i 6390-carbon-stores",   shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    cluster_name = cluster_name.replace("\n", " ")
    cluster_name = list(cluster_name.split(" "))
    print("The list of the clusters is: ", cluster_name)

elif RANCHER_ENV == "stage":
    cluster_name = subprocess.Popen("rancher clusters list | awk {'print $3'} | grep -i 4105-carbon-stores ; rancher clusters list | awk {'print $4'} | grep -i 4105-carbon-stores", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    cluster_name = cluster_name.replace("\n", " ")
    cluster_name = list(cluster_name.split(" "))
    print("The list of the clusters is: ", cluster_name)

elif RANCHER_ENV == "pre-prod":
    cluster_name = subprocess.Popen("rancher clusters list | awk {'print $3'} | grep -i 6339-carbon-stores ; rancher clusters list | awk {'print $4'} | grep -i 6339-carbon-stores", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    cluster_name = cluster_name.replace("\n", " ")
    cluster_name = list(cluster_name.split(" "))
    print("The list of the clusters is: ", cluster_name)

else:
    print("You are using wrong argument, please use one of: (sbx, dev, rona, stage, preprod)")
    exit()


# Iterate thru list of cluster and apply the changes.
for i in cluster_name:
    CLUSTER_NAME = i
    print('Current cluster name current is ' + CLUSTER_NAME)
    # Configure backend.tfvars.
    os.system("sed -i 's/.*\/terraform\/state\/carbon\/stores\/.*$/prefix = \"\/terraform\/state\/carbon\/stores\/" + RANCHER_ENV + "-user-creation\/" + CLUSTER_NAME +"\"/g' user_access/" + RANCHER_ENV + "/backend.tfvars")
    
    # Configure variables.tf.
    os.system("sed -i 's/.*cluster_name.*$/cluster_name = \"" + CLUSTER_NAME + "\"/g' user_access/" + RANCHER_ENV + "/variables.tfvars")
   
    print("")
    cat_var = run( [ 'cat', 'user_access/' + RANCHER_ENV + '/variables.tfvars'] )
    if cat_var.returncode != 0:
        raise Exception( f'ERROR cannot cat variables.tfvars: { cat_var.returncode }' )


    print('''
    *****************************************************
    *                                                   *
    *                  Terraform init                   *
    *                                                   *
    *****************************************************

    ''')

    print("")
    print("Running terraform init for " + CLUSTER_NAME )
    print("")

    tf_init = run( [ 'terraform', 'init', '-backend-config=user_access/' + RANCHER_ENV + '/backend.tfvars', '-reconfigure', 'user_access/'] )
    if tf_init.returncode != 0:
        raise Exception( f'ERROR terraform init failed: { tf_init.returncode }' )
    

    print('''
    *****************************************************
    *                                                   *
    *                  Terraform plan                   *
    *                                                   *
    *****************************************************

    ''')

    print("")
    print("Running terraform plan for " + CLUSTER_NAME )
    print("")

    tf_plan = run( [ 'terraform', 'plan', '-var-file=user_access/' + RANCHER_ENV + '/variables.tfvars',  '-var-file=user_access/' + RANCHER_ENV + '/group_id.tfvars', 'user_access/'] )
    if tf_plan.returncode != 0:
        raise Exception( f'ERROR terraform plan failed: { tf_plan.returncode }' )

    print("")


    print('''
    *****************************************************
    *                                                   *
    *                Terraform destroy                  *
    *                                                   *
    *****************************************************

    ''')
    print("")
    print("Running terraform destroy for " + CLUSTER_NAME )
    print("")

    tf_apply = run( [ 'terraform', 'destroy', '-input=false', '-auto-approve', '-var-file=user_access/' + RANCHER_ENV + '/variables.tfvars',  '-var-file=user_access/' + RANCHER_ENV + '/group_id.tfvars', 'user_access/'] )
    if tf_apply.returncode != 0:
        raise Exception( f'ERROR terraform destroy failed: { tf_apply.returncode }' )


    print('''
    *****************************************************
    *                                                   *
    *                  Terraform apply                  *
    *                                                   *
    *****************************************************

    ''')
    print("")
    print("Running terraform apply for " + CLUSTER_NAME )
    print("")

    tf_apply = run( [ 'terraform', 'apply', '-input=false', '-auto-approve', '-var-file=user_access/' + RANCHER_ENV + '/variables.tfvars',  '-var-file=user_access/' + RANCHER_ENV + '/group_id.tfvars', 'user_access/'] )
    if tf_apply.returncode != 0:
        raise Exception( f'ERROR terraform apply failed: { tf_apply.returncode }' )
