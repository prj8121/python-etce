FROM centos:7

#RUN yum -y update

#RUN yum clean all

RUN yum -y install automake autotools libtool make rpm-build python-setuptools epel-release git

WORKDIR /opt
RUN git clone https://github.com/eschreiber/python-etce -b develop

WORKDIR python-etce
RUN ./autogen.sh
RUN ./configure
RUN make rpm

RUN echo 'centos7 complete'

