####################################
#BeamNameAdjust.py
#write secondary script that adjust beam names
#
#Modified:
#2016 10 v0 Becket Hui
####################################
import re, sys  # need regex and sys, sys is needed whenever we need to pass variables from terminal
# main function
def main(savFolder, beamID = None, beamName = None, init = False, remove = False, add = False):
 if init:
  # reinitialize the secondary script, the secondary script is saved in the patient folder
  fw = open(savFolder+'BeamNameAdjust.Script','w')
  fw.write('///////////////////////////\n')
  fw.write('///BeamNameAdjust.Script///\n')
  fw.write('///////////////////////////\n')
  fw.write('\n')
  fw.close()

 if remove:
  fw = open(savFolder+'BeamNameAdjust.Script', 'a')
  if beamID != '':
   beamNameNew = re.sub(beamID, '', beamName)  # remove beam id
   beamNameNew = re.sub('^[^a-zA-Z]*','',beamNameNew)  # remove any non-character
   fw.write('TrialList.Current.BeamList.Current = \"%s\";\n' %beamName)
   fw.write('TrialList.Current.BeamList.Current.Name = \"%s\";\n' %beamNameNew)
  fw.close()

 if add:
  fw = open(savFolder+'BeamNameAdjust.Script', 'a')
  if beamID != '':
   beamNameNew = beamID + ' ' + beamName  # add beam id
   fw.write('TrialList.Current.BeamList.Current = \"%s\";\n' %beamName)
   fw.write('TrialList.Current.BeamList.Current.Name = \"%s\";\n' %beamNameNew)
  fw.close()

# this following part is needed for python code that is called in terminal
if __name__ == "__main__":
 print(sys.argv)
 savFolder = str(sys.argv[1])
 arg = str(sys.argv[-1])  #last argument determines whether to inititate, add or remove
 if arg == 'Init':
  main(savFolder, init = True)
 elif arg == 'Remove':
  main(savFolder, beamID=str(sys.argv[2]), beamName=str(sys.argv[3]), remove = True)
 elif arg == 'Add':
  main(savFolder, beamID=str(sys.argv[2]), beamName=str(sys.argv[3]), add = True)
