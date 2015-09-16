#!/bin/sh
ruby -e "$(curl -fsSL "https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap caskroom/cask
brew install caskroom/cask/brew-cask
brew cask --caskroom=/Applications
brew cask install google-chrome
brew cask install vlc
brew cask install dropbox
brew cask install the-unarchiver
brew cask install growl-notify
brew cask install quicksilver
brew cask cleanup

