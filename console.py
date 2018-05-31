# Date: 05/31/2018
# Author: Pure-L0G1C
# Description: Console Application

from sys import version 
from platform import system
from os import chdir, getcwd, system as sys_shell 

try:
 from subprocess import getoutput as shell
except ImportError:
 from subprocess import check_output as shell

class Console(object):

 __version__ = 0.1
 __date__ = '05/31/2018' 
 __author__ = 'Mohamed Sheikh'
 __description__ = 'Console Application'

 def __init__(self):
  self.LINE = '-'
  self.EDGES = '+'
  self.DEBUG = False 
  self.MAX_SIZE = 50
  self.prompt = '$> '
  self.is_alive = True 
  self.TABS_AMOUNT = 5
  self.home = getcwd()
  self.default_to_shell = True 
  self.cmds = { 'help': self._help } 
  self.BANNER = 'Possible Commands (type help <command>)'
  self.input = raw_input if self.version == 2 else input 
  self.INTRO = '{0}type help for help{0}'.format('\n\n\t')
  self.cls_cmd = 'cls' if system() == 'Windows' else 'clear'

 @property
 def version(self):
  return int(version.split()[0].split('.')[0]) 

 def shell(self, cmds):
  if cmds.split()[0].lower() == 'cd':
   path = cmds.split()[1] if len(cmds.split()) > 1 else self.home
   try:chdir(path)
   except FileNotFoundError:pass  
  else:
   print('{0}{1}{0}'.format('\n', shell([cmds]) if self.version == 2 else shell(cmds)))

 def set_cmds(self):

  # find all function which begin with cmd_      
  cmd_funcs = [item for item in dir(self) if callable(getattr(self, item)) 
              if not all([item.startswith('__'), item.endswith('__')]) 
              if item.startswith('cmd_')]
     
  # reassign names 
  for func in cmd_funcs:
   name = func.split('cmd_')[1].lower()
   self.cmds[name] = getattr(self, func)

 def cmd_cls(self, *args):
  '''Description: clear the screen\nUsage: cls'''
  sys_shell(self.cls_cmd)

 def cmd_exit(self, *args):
  '''Description: to quit the console\nUsage: quit\nUsage: exit'''

  self.stop_loop()

 def cmd_quit(self, *args):
  '''Description: to quit the console\nUsage: quit\nUsage: exit'''

  self.stop_loop() 

 def _help(self, *args):
  '''Description: to display help\nUsage: help <command>\nUsage: help'''

  if not len(args):
   self.help_menu()
  else:
   func_name = args[0][0]
   if func_name in self.cmds:
    doc = self.cmds[func_name].__doc__

    if not doc:
     print('{0}{1} is not documented{0}'.format('\n\n', func_name))
    else:
     print('{0}{1}{0}'.format('\n\n', doc))    

 def help_menu(self):
  size = 0
  print('\n' + self.BANNER)
  all_cmds = sorted(self.cmds, key=len)
  cmds = '\n{}'.format(' '* int(self.TABS_AMOUNT - (self.TABS_AMOUNT * 0.5)  )) 
  print('{0}{1}{0}'.format(self.EDGES, self.LINE * self.MAX_SIZE))

  for _, cmd in enumerate(all_cmds):
   name = cmd + (' ' * self.TABS_AMOUNT)
   cmds += name 
   size += len(name)
   next_value_size = 0 if _ > len(all_cmds) else len(all_cmds[_] + (' ' * self.TABS_AMOUNT))  
   
   if (size + next_value_size)  >= self.MAX_SIZE + (self.TABS_AMOUNT * 0.8):
    size = 0
    cmds += '\n\n{}'.format(' ' * self.TABS_AMOUNT)
  print(cmds + '\n')   

 def stop_loop(self):
  self.is_alive = False

 def user_input(self):
  user_input = self.input(self.prompt)
  if not len(user_input):
   return

  if user_input.split()[0].lower() in self.cmds:
   if len(user_input.split()) > 1:
    func = self.cmds[user_input.split()[0].lower()]
    args = ' '.join(user_input.split()[1:])
    func(args.split())
   else:
    func = self.cmds[user_input.split()[0].lower()]
    func()
  else:
   if self.default_to_shell:
    self.shell(user_input)

 def debug_mode(self):
  while self.is_alive:
   self.user_input()

 def user_mode(self):
  while self.is_alive:
   try:self.user_input()
   except:pass

 def start_loop(self):
  self.set_cmds()
  print(self.INTRO)
  self.debug_mode() if self.DEBUG else self.user_mode()   