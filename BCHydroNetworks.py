import networkx as nx
import matplotlib.pyplot as plt
##BC 

BC=nx.MultiGraph()
color_map=[]
##Microwave Stations
BC.add_edge('PMY','SMB',link='Microwave')
BC.add_edge('SMB','SLL',link='Microwave')
BC.add_edge('SLL','STE',link='Microwave')
BC.add_edge('SMB','JAR',link='Microwave')
BC.add_edge('JAR','TYN',link='Microwave')
BC.add_edge('TYN','HAM',link='Microwave')
BC.add_edge('HAM','TUK',link='Microwave')
BC.add_edge('TUK','MSV',link='Microwave')
BC.add_edge('TUK','SSR',link='Microwave')
BC.add_edge('SSR','SCI',link='Microwave')
BC.add_edge('SSR','OKN',link='Microwave')
BC.add_edge('SCI','SRG',link='Microwave')
BC.add_edge('SRG','HLL',link='Microwave')
BC.add_edge('SRG','BLZ',link='Microwave')
BC.add_edge('HLL','BKR',link='Microwave')
BC.add_edge('BKR','MRR',link='Microwave')
BC.add_edge('MRR','MAB',link='Microwave')
BC.add_edge('SSR','SLE',link='Microwave')
BC.add_edge('SLE','GDS',link='Microwave')
BC.add_edge('GDS','FLG',link='Microwave')
BC.add_edge('EMW','PMY',link='Microwave')
BC.add_edge('PMY','BWN',link='Microwave')
BC.add_edge('BWN','CTL',link='Microwave')
BC.add_edge('CTL','BRU',link='Microwave')
BC.add_edge('BRU','VCR',link='Microwave')
BC.add_edge('VCR','HSY',link='Microwave')
BC.add_edge('PCH','CTL',link='Microwave')
BC.add_edge('JHM','PCH',link='Microwave')
BC.add_edge('BWN','TSK',link='Microwave')
BC.add_edge('TSK','DCY',link='Microwave')
BC.add_edge('DCY','MSN',link='Microwave')
BC.add_edge('MSN','CRN',link='Microwave')
BC.add_edge('CRN','MSV',link='Microwave')
BC.add_edge('CRN','TIM',link='Microwave')
BC.add_edge('TIM','DGN',link='Microwave')
BC.add_edge('DGN','MMS',link='Microwave')
BC.add_edge('DGN','RRK',link='Microwave')
BC.add_edge('RRK','TBR',link='Microwave')
BC.add_edge('TBR','SRT',link='Microwave')
BC.add_edge('SRT','GNR',link='Microwave')
BC.add_edge('GNR','SNR',link='Microwave')
BC.add_edge('SNR','GRS',link='Microwave')
BC.add_edge('GRS','TKR',link='Microwave')
BC.add_edge('TKR','TPL',link='Microwave')
BC.add_edge('TPL','CPM',link='Microwave')
BC.add_edge('TBR','FTH',link='Microwave')
BC.add_edge('FTH','MRE',link='Microwave')
BC.add_edge('MRE','BOR',link='Microwave')
BC.add_edge('BOR','GWM',link='Microwave')
BC.add_edge('BOR','BLH',link='Microwave')
BC.add_edge('BLH','SUR',link='Microwave')
###Stopped at SUR because FJN is a tranmission station
BC.add_node('ESR')
BC.add_edge('PLM','BMN', link='Microwave')

microamt =len(list(BC.node())) ##amount of microwave stations
for n1 in list(BC.node()):
    BC.node[n1]['station'] ='Microwave'

##Transmission Stations 
##Cluster 1
BC.add_edge('GRS','TKW',link='Low-Capacity Radio') 
BC.add_edge('CPM','MIN',link='Microwave')
BC.add_edge('CPM','SKA',link='Low-Capacity Radio')
BC.add_edge('SKA','RUP',link='PLC')
BC.add_edge('RUP','OFD',link='Leased')
BC.add_edge('SKA','AYH',link='Fibre')
BC.add_edge('AYH','ORD',link='Fibre')
BC.add_edge('ORD','BQN',link='Fibre')
BC.add_edge('BQN','TAT',link='Fibre')
BC.add_edge('AYH','LNT',link='PLC')
BC.add_edge('LNT','STW',link='Fibre')
BC.add_edge('GNR','GLN',link='Fibre')
BC.add_edge('GLN','TPY',link='PLC')
BC.add_edge('GLN','TAC',link='PLC')
BC.add_edge('TAC','VDF',link='Leased')
BC.add_node('PCA')
BC.add_node('PGG')
BC.add_node('FHS')
BC.add_edge('FTH','KDS',link='Microwave')
BC.add_edge('KDS','MEE',link='PLC')
BC.add_edge('GWM','SNK',link='Microwave')
BC.add_edge('GWM','MKT',link='Microwave')
BC.add_edge('GWM','TLR',link='Microwave')
BC.add_edge('GWM','CWD',link='Microwave')
BC.add_edge('CWD','SLS',link='Microwave')
BC.add_edge('SLS','SGB',link='Fibre')
BC.add_edge('SGB','BMT',link='Fibre')
BC.add_edge('BMT','DAW',link='Fibre')
BC.add_edge('BMN','DAW',link='Microwave')
BC.add_edge('SUR','FJN',link='Microwave')
BC.add_edge('FJN','TAY',link='Microwave')
BC.add_edge('FJN','PLM',link='Microwave')
##BC.add_node('PPS') Island Node
BC.add_edge('TBR','WSN',link='PLC')
BC.add_edge('WSN','KDY',link='PLC')
BC.add_edge('WSN','CHO',link='PLC')
BC.add_edge('WSN','BVY',link='PLC')
BC.add_edge('WSN','CHF',link='PLC')
BC.add_edge('WSN','SVY',link='PLC')
BC.add_edge('DGN','BLW',link='Microwave')
BC.add_edge('BLW','QNL',link='Leased')
BC.add_edge('BLW','RBF',link='Leased')
BC.add_edge('RBF','BLW',link='PLC')
BC.add_edge('MMS','OLS',link='Fibre')
BC.add_edge('OLS','SCK',link='PLC')
BC.add_edge('TIM','SCK',link='Microwave')
BC.add_edge('SCK','WLM',link='Leased')## Two Leased links
BC.add_edge('SCK','HMH',link='PLC')
BC.add_edge('HMH','KLY',link='PLC')
BC.add_edge('CRN','KLY',link='Microwave')
BC.add_node('PEM')
BC.add_edge('TSK','FCN',link='Microwave')
BC.add_edge('FCN','RBW',link='PLC')
BC.add_edge('TSK','CKY',link='Microwave')
BC.add_edge('CKY','CK5',link='Fibre')
BC.add_edge('CKY','SOH',link='Leased')
BC.add_edge('BWN','GIB',link='Low-Capacity Radio')
BC.add_edge('GIB','SEC',link='PLC')
BC.add_edge('PCH','MS',link='Microwave')
BC.add_edge('MS','GRT',link='PLC')
BC.add_edge('GRT','FVW',link='Leased')
BC.add_edge('PCH','CCB',link='Microwave')
BC.add_node('TXW')
BC.add_node('OYR')
BC.add_node('CBL')
BC.add_node('CMX')
BC.add_edge('PCH','DMR',link='Microwave')
BC.add_edge('DMR','NCT',link='PLC')
BC.add_edge('DMR','GLD',link='PLC')
BC.add_edge('GLD','TSV',link='PLC')
BC.add_edge('GLD','TAH',link='Leased')
BC.add_edge('GLD','KTS',link='PLC')
BC.add_edge('KTS','KGH',link='PLC')
BC.add_edge('KGH','PHY',link='PLC')
BC.add_edge('KGH','JUL',link='Leased')
BC.add_edge('JUL','GLD',link='Leased')
BC.add_edge('DMR','PAL',link='Leased')
BC.add_edge('PAL','GCL',link='Leased')
BC.add_node('NFD')
BC.add_node('PVD')
BC.add_node('HWD')
BC.add_node('LDY')
BC.add_edge('CTL','JPT',link='Microwave')
BC.add_edge('JPT','QLC',link='Leased')
BC.add_edge('JPT','LTZ',link='Leased')
BC.add_edge('BRU','ARN',link='Microwave')
BC.add_edge('ARN','EBT',link='Leased')
BC.add_edge('ARN','CPT',link='Leased')
BC.add_edge('CPT','ARN',link='Leased')
BC.add_edge('ARN','SYR',link='Fibre')
BC.add_edge('SYR','ING',link='Fibre')
BC.add_edge('PMY','ING',link='Microwave')
BC.add_edge('BRU','VIT',link='Microwave')
BC.add_edge('VIT','CFT',link='Leased')
BC.add_edge('VIT','KSH',link='Leased')
BC.add_edge('VIT','SHA',link='Leased')
BC.add_edge('VIT','SAL',link='PLC')
BC.add_edge('VIT','TRN',link='PLC')
BC.add_edge('TRN','GLS',link='PLC')
BC.add_edge('BRU','SAT',link='Microwave')
BC.add_edge('VCR','OBW',link='Fibre')
BC.add_edge('VCR','T2K',link='Microwave')
BC.add_edge('T2K','CLD',link='Fibre')
BC.add_edge('CLD','SOO',link='PLC')
BC.add_edge('HSY','ESQ',link='Fibre')
BC.add_edge('HSY','GTP',link='Fibre')
BC.add_edge('BRU','KTG',link='Low-Capacity Radio')
BC.add_edge('KTG','SNY',link='PLC')
BC.add_edge('BWN','TBY',link='Low-Capacity Radio')
BC.add_edge('BWN','SEP',link='Microwave')
BC.add_edge('TSK','TIS',link='Microwave')
BC.add_edge('MSN','BRT',link='Microwave')
BC.add_edge('PMY','WLT',link='Low-Capacity Radio')
BC.add_edge('WLT','DCV',link='Leased')
BC.add_edge('WLT','CAP',link='Leased')
BC.add_edge('WLT','LYN',link='Fibre')
BC.add_edge('WLT','NOR',link='Leased')
BC.add_edge('WLT','NVR',link='Leased')
BC.add_edge('WLT','JUN',link='Leased')
BC.add_edge('WLT','HSB',link='Leased')
BC.add_edge('HSB','LBY',link='Leased')
BC.add_edge('EMW','DGR',link='Fibre')
BC.add_edge('DGR','MUR',link='Fibre')
BC.add_edge('MUR','HPN',link='Fibre')
BC.add_edge('HPN','CSQ',link='Fibre')
BC.add_edge('HPN','NEL',link='Fibre')
BC.add_edge('NEL','LMC',link='Fibre')
BC.add_edge('NEL','SDM',link='Fibre')
BC.add_edge('LMC','SDM',link='Fibre')
BC.add_edge('LMC','MAN',link='Fibre')
BC.add_edge('MAN','KI1',link='Fibre')
BC.add_edge('KI1','KI2',link='Fibre')
BC.add_edge('KI2','CAM',link='Fibre')
BC.add_edge('CAM','SDM',link='Low-Capacity Radio')
BC.add_edge('SDM','S1V',link='Low-Capacity Radio')
BC.add_edge('SDM','ANN',link='Low-Capacity Radio')
BC.add_edge('SDM','MDN',link='Microwave')
BC.add_edge('PMY','SDM',link='Low-Capacity Radio')
BC.add_edge('PMY','MDN',link='Fibre')
BC.add_edge('HPN','BND',link='Fibre')
BC.add_edge('BND','COK',link='Fibre')
BC.add_edge('COK','WHY',link='Fibre')
BC.add_edge('LMC','MAN',link='Fibre')
BC.add_node('FLW')
BC.add_edge('SMB','MLN',link='Microwave')
BC.add_edge('MLN','NKL',link='Leased')
BC.add_edge('SMB','CBN',link='Microwave')
BC.add_edge('CBN','GLT',link='Leased')
BC.add_edge('SMW','ABT',link='Leased')
BC.add_edge('SMB','AL2',link='Microwave')
BC.add_node('CHK') 
BC.add_edge('SMB','RCC',link='Microwave')
##BC.add_node('MRG') Island Node
BC.add_edge('RCC','KEN',link='Leased')
BC.add_node('SVD')
BC.add_node('SFY')
BC.add_edge('STE','UHT',link='Microwave')
BC.add_edge('JAR','AMC',link='Microwave')
BC.add_edge('AMC','BBR',link='Leased')
BC.add_edge('AMC','CHP',link='Fibre')
BC.add_edge('AMC','HCP',link='Leased')
BC.add_edge('HAM','NIC',link='Microwave')
BC.add_edge('NIC','PRI',link='PLC')
BC.add_edge('MSV','GUI',link='Microwave')
BC.add_node('WBK')
BC.add_edge('INT','LDE',link='PLC')
BC.add_edge('INT','MON',link='PLC')
BC.add_edge('INT','LOO',link='PLC')
BC.add_edge('OKN','W11',link='Microwave')
BC.add_edge('BLZ','ESS',link='Microwave')
BC.add_edge('BLZ','SL1',link='Microwave')
BC.add_edge('BLZ','NLY',link='Microwave')
BC.add_edge('BKR','CSR',link='Microwave')
BC.add_edge('CSR','AAL',link='PLC')
BC.add_edge('CSR','INV',link='PLC')
BC.add_edge('CSR','SPL',link='Leased')
BC.add_edge('CSR','NT2',link='PLC')
BC.add_edge('CSR','KBY',link='PLC')
BC.add_node('NTL')
BC.add_node('JOE')
BC.add_node('ILL')
##BC.add_edge('VLM','AVO',link='Leased') Two Island Nodes
BC.add_edge('TUK','ACK',link='Microwave')
BC.add_edge('ACK','SAM',link='PLC')
BC.add_edge('MSV','SVA',link='Microwave')
BC.add_edge('SVA','HLD',link='PLC')
BC.add_edge('SVA','BKL',link='Low-Capacity Radio')
BC.add_edge('MSV','VVW',link='Microwave')
BC.add_edge('VVW','KWD',link='Leased')
BC.add_edge('KWD','VVW',link='Leased')
BC.add_edge('VVW','DUG',link='Leased')
BC.add_edge('DUG','VVW',link='Leased')

transamt = len(list(BC.node()))-microamt
n=1
for n1 in list(BC.node()):
    if n>microamt:
        BC.node[n1]['station']='Transmission'
    n+=1
##Generating Stations
BC.add_edge('RUP','FLS',link='PLC')
BC.add_edge('BLH','GMS',link='Microwave')
##BC.add_node('MCM') Island Node
BC.add_edge('BLH','PCN',link='Microwave')
BC.add_edge('FJO','PCN',link='Leased')
BC.add_edge('TSK','CMS',link='Microwave')
BC.add_edge('SOH','MAM',link='Leased')
BC.add_edge('SEC','SOM',link='PLC')
BC.add_edge('JHM','JHT',link='Fibre')
BC.add_edge('PUN','JHT',link='PLC')
BC.add_edge('JHT','PUN',link='Leased')
BC.add_edge('CBL','JHT',link='Leased')
BC.add_edge('CMX','JHT',link='Leased')
BC.add_edge('JHT','LDR',link='Fibre')
BC.add_edge('LDR','SCA',link='PLC')
BC.add_edge('GLD','SCA',link='PLC')
BC.add_edge('OYR','JHT',link='Leased')
BC.add_edge('GCL','ASH',link='PLC')
BC.add_edge('SOO','JOR',link='PLC')
BC.add_edge('PMY','BSY',link='Microwave')
BC.add_edge('RCC','NAH',link='Fibre')
BC.add_edge('SMB','RUS',link='Microwave')
BC.add_edge('SVD','RUS',link='Fibre')
BC.add_edge('SFY','RUS',link='Fibre')
BC.add_edge('SFY','SFW',link='Fibre')
BC.add_edge('SFY','SFN',link='Fibre')
BC.add_edge('SFN','ALU',link='PLC')
BC.add_node('LAJ')
BC.add_node('SON')
BC.add_edge('BLZ','WAN',link='Microwave')
BC.add_edge('BLZ','SEV',link='Microwave')
BC.add_edge('SRG','KO',link='Microwave')
BC.add_edge('CSR','ELK',link='PLC')
BC.add_edge('CSR','ABF',link='PLC')
BC.add_edge('SLE','REN',link='Microwave')
BC.add_edge('REN','ILL',link='PLC')
BC.add_edge('FLG','MCA',link='Microwave')

genamt = len(list(BC.node()))-microamt-transamt
n=1
for n1 in list(BC.node()):
    if n>(microamt+transamt):
        BC.node[n1]['station']='Generating'
    n+=1
    
##Offices
BC.add_edge('CPM','TRO',link='Microwave')
BC.add_edge('TBR','PGO',link='Microwave')
BC.add_edge('PGG','PGO',link='Leased')
BC.add_edge('PCA','PGO',link='Leased')
BC.add_edge('FHS','PGO',link='Leased')
BC.add_edge('BLW','QNL-DO',link='Leased')
BC.add_edge('SCK','WLO',link='Leased')
BC.add_edge('WLO','WLM',link='Leased')
BC.add_edge('WLM','SCK',link='Leased')
BC.add_edge('SCK','WLM',link='Leased')
BC.add_edge('CKY','SQO',link='Leased')
BC.add_edge('FVW','PDO',link='PLC')
##BC.add_node('CDO') Island Node
BC.add_edge('JHT','CLR',link='Leased')
BC.add_edge('JPT','NAN',link='Fibre')
BC.add_edge('NFD','NAN',link='Leased')
BC.add_edge('LDY','NAN',link='Leased')
BC.add_edge('PAL','NAN',link='Leased')
BC.add_edge('HWD','NAN',link='Leased')
BC.add_edge('PVD','NAN',link='Leased')
BC.add_edge('NAN','CTO',link='Leased')
BC.add_edge('NAN','QAL',link='Leased')
BC.add_edge('VIT','DDO',link='Leased')
BC.add_edge('OBW','ROY',link='Fibre')
BC.add_edge('BRU','GDO',link='Leased')
BC.add_edge('GDO','BRU',link='Leased')
BC.add_edge('CSQ','DUN',link='Fibre')
BC.add_edge('CBN','ABS',link='Leased')
BC.add_edge('SMW','ABS',link='Leased')
BC.add_edge('AL2','FVE',link='Leased')
BC.add_edge('FVE','AL2',link='Leased')
BC.add_edge('CHK','FVE',link='Leased')
##BC.add_edge('MRG','RSO',link='Leased') Two Island Nodes
BC.add_edge('AMC','HDL',link='Leased')
BC.add_edge('WLT','NVU',link='Leased')
BC.add_edge('LLO','SON',link='Leased')
BC.add_edge('MSN','LLO',link='Leased')
BC.add_node('CIO')
BC.add_edge('BKR','CBO',link='Microwave')
BC.add_edge('NTL','CBO',link='Leased')
BC.add_edge('JOE','CBO',link='Leased')
##BC.add_edge('GDN','GDNO',link='Leased') Two Island Nodes
##BC.add_node('SAO') Island Node
BC.add_edge('DUG','KAM',link='Leased')
BC.add_node('FJO')

offamt = len(list(BC.node()))-microamt-transamt-genamt
n=1
for n1 in list(BC.node()):
    if n>(microamt+transamt+genamt):
        BC.node[n1]['station']='Office'
    n+=1
    
##Repeaters
BC.add_edge('PAL','PAO',link='Leased')
BC.add_edge('ROY','MTD',link='Leased')
BC.add_edge('MSN','MTO',link='Low-Capacity Radio')
BC.add_edge('LAJ','MTO',link='Low-Capacity Radio')
BC.add_edge('LAJ','BRK',link='PLC')
BC.add_edge('BRT','BRK',link='Fibre')
BC.add_edge('BRT','BH2',link='Fibre')
##BC.add_node('MOT') ISLAND NODE
BC.add_node('SHO')
BC.add_edge('KO','KLS',link='Leased')
BC.add_edge('KO','CIO',link='Leased')

repamt = len(list(BC.node()))-microamt-transamt-genamt-offamt
n=1
for n1 in list(BC.node()):
    if n>(microamt+transamt+genamt+offamt):
        BC.node[n1]['station']='Repeater'
    n+=1
    
##Control Centers
BC.add_edge('PMY','FVO',link='Microwave')
BC.add_edge('MLN','FVO',link='Fibre')
BC.add_node('SIO')

n=1
contamt = len(list(BC.node()))-microamt-transamt-genamt-offamt-repamt
for n1 in list(BC.node()):
    if n>(microamt+transamt+genamt+offamt+repamt):
        BC.node[n1]['station']='Control'
    n+=1
##Other
BC.add_edge('TAT','RDC',link='Fibre') 
BC.add_edge('BQN','FKR',link='Fibre')
BC.add_edge('LNT','BJT',link='Fibre')
BC.add_edge('LNT','LNL',link='Fibre')
BC.add_edge('MIN','KIT',link='Fibre')
BC.add_edge('KIT','MIN',link='Fibre')
BC.add_edge('KIT','KMO',link='PLC')
BC.add_edge('KMO','KIT',link='PLC')
BC.add_edge('TSK','CRK',link='Microwave')
BC.add_edge('PEM','CRK',link='Fibre')
BC.add_edge('CRK','PEM',link='Leased')
BC.add_edge('PEM','MCP',link='Fibre')
BC.add_edge('SOH','FRI',link='Leased')
BC.add_edge('DUG','KAM',link='Leased')
BC.add_edge('MS','HSP',link='PLC')
BC.add_edge('PCH','TIR',link='Microwave')
BC.add_edge('TXW','TIR',link='PLC')
BC.add_edge('TXE','TIR',link='PLC')
BC.add_edge('JHT','EFM',link='Leased')
BC.add_edge('JHT','ICG',link='Fibre')
BC.add_edge('ICG','EFM',link='Fibre')
BC.add_edge('KTS','KKS',link='Fibre')
BC.add_edge('JPT','HMC',link='Leased')
BC.add_edge('HSY','VI-MAN',link='Leased')
BC.add_edge('ESQ','BNT',link='Leased')
BC.add_edge('BND','MCC',link='Fibre')
BC.add_edge('NAH','NLK',link='Fibre')
BC.add_edge('SFY','SFR',link='Fibre')
BC.add_edge('SFY','SFI',link='Fibre')
BC.add_edge('UHT','KWL',link='Fibre')
BC.add_edge('BBR','SZY',link='Leased')
BC.add_edge('TIS','BDH',link='Fibre')
BC.add_edge('TIS','UHR',link='Fibre')
BC.add_edge('SSR','SIC',link='Microwave')
BC.add_edge('SHO','SIC',link='Leased')
BC.add_edge('WBK','SIC',link='Leased')
BC.add_edge('INT','SIC',link='Fibre')
BC.add_edge('SIO','SIC',link='Fibre')
BC.add_edge('CBO','CRS',link='Leased')
BC.add_edge('KBY','CRS',link='Leased')
BC.add_edge('KWD','WEY',link='Fibre')
BC.add_edge('TLR','QTY',link='Fibre')
BC.add_edge('QTY','TLR',link='Fibre')
BC.add_edge('MKT','MKW',link='Fibre')
BC.add_edge('MKW','MKT',link='Fibre')
BC.add_edge('BOR','DKT',link='Microwave')
BC.add_edge('DKT','DKW',link='Fibre')
BC.add_edge('FJN','FJN-DO', link='Leased')
BC.add_edge('PLM','PLD',link='Fibre')
BC.add_edge('PLD','PLM',link='Fibre')
BC.add_edge('BMT','BMW',link='Fibre')
BC.add_edge('BMN','SGP',link='Microwave')
BC.add_edge('BMT','E42',link='Microwave')
BC.add_edge('ESR','E42',link='Microwave')
BC.add_edge('ESR','KIS',link='Microwave')
BC.add_edge('KIS','E15',link='Fibre')
BC.add_edge('E15','KIS',link='Fibre')
BC.add_edge('KIS','ET3',link='Microwave')

n=1
othamt = len(list(BC.node()))-microamt-transamt-genamt-offamt-repamt-contamt
for n1 in list(BC.node()):
    if n>(microamt+transamt+genamt+offamt+repamt+contamt):
        BC.node[n1]['station']='Other'
    n+=1   
    
##Connector
BC.add_edge('WHY','Connector',link='Fibre')
BC.add_edge('ING','Connector',link='Fibre')
BC.add_edge('FLW','Connector',link='Fibre')
BC.add_edge('FVO','Connector',link='Fibre')
BC.add_edge('SMB','BPA/Cluster',link='Microwave')
BC.add_edge('NLY','BPA/Boundary',link='Microwave')
n=1
connectamt =len(list(BC.node()))-microamt-transamt-genamt-offamt-repamt-contamt-othamt
for n1 in list(BC.node()):
    if n>(microamt+transamt+genamt+offamt+repamt+contamt+othamt):
        BC.node[n1]['station']='Connector'
    n+=1   
for n1 in list(BC.node()):
    if BC.node[n1].get('station')=='Microwave':
        color_map.append('red')
    elif BC.node[n1].get('station')=='Transmission':
        color_map.append('yellow')
    elif BC.node[n1].get('station')=='Generating':
        color_map.append('black')
    elif BC.node[n1].get('station')=='Office':
        color_map.append('green')
    elif BC.node[n1].get('station')=='Repeater':
        color_map.append('grey')   
    elif BC.node[n1].get('station')=='Control':
        color_map.append('pink')  
    elif BC.node[n1].get('station')=='Other':
        color_map.append('blue') 
    elif BC.node[n1].get('station')=='Connector':
        color_map.append('indigo')     
    else:
        color_map.append('cyan')
color_map1=[]
microlink=0
for node1, node2, data in BC.edges(data=True):
    if(data.get('link')=='Microwave'):
        color_map1.append('blue')
        microlink+=1
    elif(data.get('link')=='PLC'):
        color_map1.append('lime')
    elif(data.get('link')=='Leased'):
        color_map1.append('black')  
    elif(data.get('link')=='Fibre'):
        color_map1.append('red')
    elif(data.get('link')=='Low-Capacity Radio'):
        color_map1.append('purple')
    else:
        color_map1.append('pink')## No edges should be pink so if pink is present that means the edge isnt correctly named
plt.figure(figsize=(16,16)) 
pos = nx.kamada_kawai_layout(BC)
##LEGEND
##Nodes
nx.draw_networkx_nodes(BC,pos=pos,node_color='red',node_size=90,label='Microwave Station')
nx.draw_networkx_nodes(BC,pos=pos,node_color='yellow',node_size=90, label='Transmission Station')
nx.draw_networkx_nodes(BC,pos=pos,node_color='black',node_size=90, label='Generating Station')
nx.draw_networkx_nodes(BC,pos=pos,node_color='green',node_size=90, label='Office')
nx.draw_networkx_nodes(BC,pos=pos,node_color='pink',node_size=90, label='Control Center')
nx.draw_networkx_nodes(BC,pos=pos,node_color='grey',node_size=90, label='Repeater')
nx.draw_networkx_nodes(BC,pos=pos,node_color='indigo',node_size=90, label='Connector')
nx.draw_networkx_nodes(BC,pos=pos,node_color='blue',node_size=90, label='Other')
##Links
nx.draw_networkx_edges(BC,pos=pos,edge_color='blue',edge_size=5,label='Microwave Link')
nx.draw_networkx_edges(BC,pos=pos,edge_color='lime',edge_size=5,label='PLC Link')
nx.draw_networkx_edges(BC,pos=pos,edge_color='red',edge_size=5,label='Fiber Link')
nx.draw_networkx_edges(BC,pos=pos,edge_color='black',edge_size=5,label='Leased Link')
nx.draw_networkx_edges(BC,pos=pos,edge_color='purple',edge_size=5,label='Low-Capacity Radio')
nx.draw_networkx(BC,pos, node_color=color_map,edge_color=color_map1, with_labels=False,node_size=100, width=2, font_size=6)
plt.legend(loc=2,ncol=2,fontsize=18)
plt.show()


##Simplified Network
SMP=BC.copy()
##Removes Microwave Stations with one Transmission,Generating, or Other Node attached to it
for n1 in list(SMP.nodes()):
    if SMP.node[n1].get('station')=='Microwave':
        other=0
        temp='none'
        for n2 in list(SMP.neighbors(n1)):
            if SMP.node[n2].get('station')!='Microwave':
                other+=1
                temp=n2
        if (other==1):
            for n2 in list(SMP.neighbors(n1)):
                SMP.add_edge(temp,n2)
            SMP.remove_node(n1)
##Simplification Process
for n1 in list(SMP.nodes()):
    if SMP.node[n1].get('station')=='Microwave':
        Slist=list(SMP.neighbors(n1))
        for n2 in Slist:
            if(Slist.index(n2)==0):
                firstnode=n2
                temp=n2
            elif(Slist.index(n2)==(len(Slist)-1)):
                SMP.add_edge(firstnode,n2)
            else:
                SMP.add_edge(temp,n2)
                temp=n2
        SMP.remove_node(n1)
color_map2=[]
for n1 in list(SMP.node()):
    if SMP.node[n1].get('station')=='Microwave':
        color_map2.append('red')
    elif SMP.node[n1].get('station')=='Transmission':
        color_map2.append('yellow')
    elif SMP.node[n1].get('station')=='Generating':
        color_map2.append('black')
    elif SMP.node[n1].get('station')=='Office':
        color_map2.append('lime')
    elif SMP.node[n1].get('station')=='Repeater':
        color_map2.append('grey')   
    elif SMP.node[n1].get('station')=='Control':
        color_map2.append('pink')  
    elif SMP.node[n1].get('station')=='Other':
        color_map2.append('blue') 
    elif SMP.node[n1].get('station')=='Connector':
        color_map2.append('indigo')     
    else:
        color_map2.append('cyan')        
plt.figure(figsize=(16,16)) 
pos = nx.kamada_kawai_layout(SMP)
##LEGEND
##Nodes
nx.draw_networkx_nodes(SMP,pos=pos,node_color='yellow',node_size=90, label='Transmission Station')
nx.draw_networkx_nodes(SMP,pos=pos,node_color='black',node_size=90, label='Generating Station')
nx.draw_networkx_nodes(SMP,pos=pos,node_color='green',node_size=90, label='Office')
nx.draw_networkx_nodes(SMP,pos=pos,node_color='pink',node_size=90, label='Control Center')
nx.draw_networkx_nodes(SMP,pos=pos,node_color='grey',node_size=90, label='Repeater')
nx.draw_networkx_nodes(SMP,pos=pos,node_color='indigo',node_size=90, label='Connector')
nx.draw_networkx_nodes(SMP,pos=pos,node_color='blue',node_size=90, label='Other')
nx.draw_networkx(SMP,pos,node_color=color_map2, with_labels=False,node_size=100, width=2, font_size=12)
plt.legend(loc=1,ncol=2,fontsize=18)
plt.show()
