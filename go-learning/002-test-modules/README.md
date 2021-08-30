Creating go project init 

go mod init example.com/username/repo


 go test
# Output should be like bellow.
 ok  	example.com/username/repo	0.095s

 go get rsc.io/quote
 go test

 # To list all dependencies inside the code.
 go list -m all


 # To list all the versions of dependency

 go list -m -versions rsc.io/sampler