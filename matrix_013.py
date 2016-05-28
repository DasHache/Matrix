# Les bases du python / math
# Les collections. 8. Rappelle
from optparse import OptionParser
import sys


# 1. 
# F.A.C.S = Facial Action Coding System
#         = est une methode de description des mouvements du visage
#           developpee par les psychologues Paul Ekman et Wallace Friesen
# (rien a voir avec Python ;-)
#
# T'as un dict des dicts:
dict_au = {  0 : {'name' : 'Neutral face',      'muscles' : 'pas de muscles qui travaillent'     },
             1 : {'name' : 'Inner Brow Raiser', 'muscles' : 'frontalis (pars medialis)'          },
             6 : {'name' : 'Cheek Raiser',      'muscles' : 'orbicularis oculi (pars orbitalis)' },
            12 : {'name' : 'Lip Corner Puller', 'muscles' : 'zygomaticus major'                  }
          }

emo_happy    = [6, 12]
emo_sad      = [1, 4, 15]
emo_surprise = []
emo_fear     = [1, 2, 4, 5, 7, 20, 26]
emo_anger    = [4, 5, 7, 23]
emo_disgust  = [9, 15, 16]
emo_contempt = []


def get_muscles(emo):
    for au in emo:
        print '  muscle: ', dict_au[au]['muscles']

def emotion2emo(emotion):
    global emo_happy, emo_sad

    if emotion == 'happy':
        return emo_happy
    if emotion == 'sad':
        return emo_sad
    else:
        return []
        
if __name__ == "__main__":
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option('-e', '--emotion', action='store', dest='emotion', default=None, help='specify an emotion')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    (options, args) = parser.parse_args()

    print 'Requested emotion: ', options.emotion
    emo = emotion2emo(options.emotion)
    print 'Corresponsing emo: ', emo
    get_muscles(emo)
    





