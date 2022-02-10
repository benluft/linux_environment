#!/bin/bash

# See https://www.java.com/en/download/help/linux_x64_install.html

mkdir /usr/java
cd /usr/java
curl -LO https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245797_df5ad55fdd604472a86a45a217032c7d

tar zxvf jre-8u73-linux-x64.tar.gz
mv AutoDL?BundleId=245797_df5ad55fdd604472a86a45a217032c7d/jre1.8.0_321 jre1.8.0_321
# rm AutoDL?BundleId=245797_df5ad55fdd604472a86a45a217032c7d
