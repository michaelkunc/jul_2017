import random
from string import ascii_uppercase, digits


class Product(object):

    FAMILIES = {1: 'Electronic Kits & Modules', 2: 'Test & Measurment', 3: 'Tools & Equipment',
                4: 'Components & Hardware'}

    SUBFAMILIES = ['Misc Electronic Components', 'Component Packs', 'Pre-Programmed Firmware',
                   'Controller Automation', 'Audio Kits', 'Sensing Device', 'Relay Board Kits',
                   'Data Loggers', 'Soldering', 'Power Inverters', 'Microcontrollers', 'Electrical Hardware',
                   'Security Kits']

    def __init__(self):
        pass

    def part_number(self):
        prefix = ''.join(random.sample(ascii_uppercase, 3))
        suffix = ''.join(random.sample(digits, 8))
        return '{0}-{1}'.format(prefix, suffix)

    def name(self):
        nouns = ('Resistor', 'Potentiometer', 'Capacitor',
                 'Inductor', 'Oscillator', 'Relay', 'Transformer', 'Battery', 'Integrated Circuit',
                 'Display', 'Condenser', 'Reactor', 'Isolator', 'Control Knob', 'PWB', 'Diode',
                 'Thermistor', 'CMOS', 'Timer', 'Comparator', 'Regulator', 'Aplifier', 'Cerebra', 'Cerebro')

        adjectives = ('Active', 'Arc', 'DC', 'Fused', 'Passive',
                      'Electromechanical', 'Constant Current', 'MOSFET', 'Incandescent',
                      'Diode', 'MIS', 'Piezoelectrical', 'Choke', 'Solenoid', 'Selenium',
                      'Distributed', 'Voltage Regulation', 'Light Emitting', 'Variable Capacitance',
                      'Carbon Film', 'Metal Film', 'Variable', 'CDS', 'NTC', 'PTC', 'CTR', 'Electrolytic',
                      'Tantalum', 'Ceramic', 'Multilayer', 'Polystyrene', 'Polypropylene', 'Mica', 'Repulsing')

        return '{0} {1}'.format(random.choice(adjectives), random.choice(nouns))

    def description(self):
        descriptions = ('FLIP-FLOP, 2 CIRCUITS', 'Logic IC Case Style',
                        'PDIP', 'No. of Pins: 14', 'Case Style: PDIP', 'Single Transmitter/Receiver',
                        'RS-422/RS-485', '8-Pin PDIP Tube', 'XOR Gate', '4-Element', '2-IN Bipolar',
                        '14-Pin PDIP,XOR Gate', '4-Element 2-IN', 'Bipolar 14-Pin', 'PDIP XOR Gate',
                        'IBUS', 'JIS', 'DC Block Type', 'Electrical Coil Sensor', 'Type 76553', 'Fiber Optic Circuit',
                        'Constant Input Resistance', 'Constant Output resistance', 'TI', 'Stark Industries Model',
                        'Reed Richards Design', 'Later Design Type', 'Reference 22320f', 'Von Doom Captive Design',
                        'McCoy Style Conversion', 'Cho Model', 'Log Counter Implementatoon', 'MK VI', 'MKVII',
                        'MacTaggert Implementation', 'Pym Particle Reduction', 'Bannertech')

        return '{0} {1}'.format(random.choice(descriptions), random.choice(descriptions))

    def uom(self):
        uoms = ('Each', 'Case', '12 Pack', 'Pallet', '24 Pack')
        return random.choice(uoms)
