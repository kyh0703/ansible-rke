# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias vi='vim -b'
alias anp='ansible-playbook'
alias ang='ansible-galaxy'

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
