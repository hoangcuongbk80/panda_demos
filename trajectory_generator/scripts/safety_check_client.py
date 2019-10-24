#!/usr/bin/env python

import sys
import rospy
from trajectory_generator.srv import *

test = [
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40724661724585409,
			0.93545642930655959,
			-0.41933662556074763,
			-1.4320075802101837,
			0.44370802224428785,
			2.2730851050738083,
			-1.7492661652753791
		],
		[
			-0.40686069447372186,
			0.93503167806532927,
			-0.41935358529341654,
			-1.4328268111078344,
			0.44372688543624811,
			2.2734571413106877,
			-1.749170959547341
		],
		[
			-0.40608924687339976,
			0.93418337240293736,
			-0.41938741760523135,
			-1.4344627785476818,
			0.44376446326042446,
			2.2742001289034817,
			-1.7489798557695679
		],
		[
			-0.40493305863438928,
			0.93291388146917054,
			-0.41943794275546026,
			-1.4369105556741588,
			0.44382046286013443,
			2.2753119914219435,
			-1.7486914157966764
		],
		[
			-0.40339315989283869,
			0.9312266155228287,
			-0.41950492075196244,
			-1.4401632556757227,
			0.44389494143925895,
			2.2767906938971234,
			-1.7483028266198442
		],
		[
			-0.4014710935840442,
			0.92912633846370429,
			-0.41958807464004227,
			-1.4442108328652283,
			0.44398661937399686,
			2.2786311796249268,
			-1.7478118618396663
		],
		[
			-0.39916868634492775,
			0.92661865203210891,
			-0.41968690581791335,
			-1.4490417039825307,
			0.4440951265011287,
			2.280829054149748,
			-1.7472146206952022
		],
		[
			-0.39648804374700342,
			0.92371021184399649,
			-0.41980089391078762,
			-1.4546420562878619,
			0.44421964993469759,
			2.2833786782970282,
			-1.7465067683611739
		],
		[
			-0.3934315260899911,
			0.92040859320190183,
			-0.41992943756774276,
			-1.4609961617541256,
			0.44435925462994985,
			2.2862736308173308,
			-1.745683309248002
		],
		[
			-0.39000170803605783,
			0.91672221451971869,
			-0.42007185792899071,
			-1.4680865343552967,
			0.44451289001368999,
			2.2895067720895068,
			-1.7447386125629567
		],
		[
			-0.38620133568171516,
			0.91266025650125338,
			-0.42022740221591798,
			-1.4758940963849652,
			0.44467939692886677,
			2.2930703113473272,
			-1.7436664392255914
		],
		[
			-0.38203328202147468,
			0.90823257906516652,
			-0.4203952473340179,
			-1.4843983498030173,
			0.4448575147056783,
			2.296955875768405,
			-1.7424599694587952
		],
		[
			-0.37750050171783106,
			0.90344963791977706,
			-0.42057450338382091,
			-1.4935775487860301,
			0.44504588818272978,
			2.3011545798372568,
			-1.7411118304120625
		],
		[
			-0.37260598602365547,
			0.89832240254227791,
			-0.42076421698418182,
			-1.5034088699551806,
			0.44524307451817186,
			2.3056570935175911,
			-1.7396141232293312
		],
		[
			-0.36735271861326901,
			0.89286227712243027,
			-0.42096337432407194,
			-1.5138685771453404,
			0.44544754965160549,
			2.3104537079301486,
			-1.737958449046181
		],
		[
			-0.36174363297451501,
			0.88708102580584869,
			-0.42117090387246342,
			-1.5249321780303571,
			0.44565771430132262,
			2.3155343974191096,
			-1.7361359334851771
		],
		[
			-0.35578157190305465,
			0.88099070333111873,
			-0.42138567869011273,
			-1.5365745704030718,
			0.44587189940672939,
			2.3208888770900415,
			-1.7341372493087612
		],
		[
			-0.34946924952814085,
			0.87460359191127313,
			-0.42160651830131707,
			-1.5487701763982566,
			0.44608837095128229,
			2.3265066551049371,
			-1.7319526369819629
		],
		[
			-0.34280921619168359,
			0.86793214497477067,
			-0.42183219009740941,
			-1.5614930634198325,
			0.44630533412588647,
			2.332377079215556,
			-1.7295719229884661
		],
		[
			-0.33580382640364381,
			0.8609889381625182,
			-0.42206141025641619,
			-1.5747170509735113,
			0.44652093681568583,
			2.3384893771981923,
			-1.7269845358304912
		],
		[
			-0.32845521000979816,
			0.85378662778191816,
			-0.42229284417464125,
			-1.5884158029996578,
			0.44673327241395849,
			2.3448326910158084,
			-1.7241795197233893
		],
		[
			-0.32076524663458256,
			0.84633791675011627,
			-0.42252510641577246,
			-1.6025629056412833,
			0.44694038198513808,
			2.3513961046742051,
			-1.7211455460686629
		],
		[
			-0.31273554340304055,
			0.83865552791817466,
			-0.42275676019144132,
			-1.6171319306651442,
			0.44714025581472139,
			2.3581686658560894,
			-1.7178709228538316
		],
		[
			-0.30436741590198835,
			0.8307521845557686,
			-0.42298631639403367,
			-1.6320964849800534,
			0.44733083439709925,
			2.3651394015106915,
			-1.714343602184321
		],
		[
			-0.29566187231088531,
			0.82264059769068842,
			-0.42321223220812532,
			-1.6474302468684237,
			0.44751000892335918,
			2.3722973276480888,
			-1.7105511862019336
		],
		[
			-0.28661960061664632,
			0.81433345993658568,
			-0.42343290933137323,
			-1.6631069896695134,
			0.44767562134018302,
			2.3796314536386896,
			-1.7064809316874849
		],
		[
			-0.27724095882250149,
			0.80584344540289876,
			-0.42364669183928688,
			-1.6791005937317545,
			0.44782546405844109,
			2.3871307813518867,
			-1.7021197536829591
		],
		[
			-0.26752596806770551,
			0.79718321525953051,
			-0.423851863731248,
			-1.6953850474933907,
			0.44795727939635177,
			2.3947842994864819,
			-1.6974542285023737
		],
		[
			-0.257474308590941,
			0.78836542852204994,
			-0.42404664619772825,
			-1.7119344385623216,
			0.44806875884748681,
			2.4025809734519852,
			-1.69247059653169
		],
		[
			-0.24708531849441112,
			0.77940275762779976,
			-0.42422919465105646,
			-1.7287229356538494,
			0.4481575422688408,
			2.4105097311570587,
			-1.6871547652478451
		],
		[
			-0.23635799529650456,
			0.77030790838605312,
			-0.42439759556461326,
			-1.7457247622152148,
			0.44822121708889234,
			2.4185594450517649,
			-1.6814923129163661
		],
		[
			-0.22529100029751364,
			0.76109364390361756,
			-0.42454986316811677,
			-1.762914162523755,
			0.44825731764039117,
			2.4267189107562861,
			-1.6754684934570909
		],
		[
			-0.2138826658240863,
			0.75177281210842928,
			-0.42468393604997384,
			-1.7802653609961234,
			0.44826332472766151,
			2.4349768225924637,
			-1.669068242998998
		],
		[
			-0.202131005463071,
			0.74235837651571501,
			-0.42479767372164218,
			-1.7977525153933394,
			0.44823666554368558,
			2.443321746317622,
			-1.6622761886786015
		],
		[
			-0.19003372744327957,
			0.73286344990223995,
			-0.4248888532037946,
			-1.8153496645541702,
			0.44817471405817971,
			2.4517420893442967,
			-1.6550766602721803
		],
		[
			-0.17758825137372175,
			0.72330133057267187,
			-0.42495516569992053,
			-1.8330306712401931,
			0.44807479200431277,
			2.4602260687158859,
			-1.6474537052902531
		],
		[
			-0.1647917285982361,
			0.71368554091676084,
			-0.42499421343002736,
			-1.8507691606324521,
			0.44793417059855162,
			2.4687616770980263,
			-1.6393911082030219
		],
		[
			-0.15164106647835568,
			0.70402986796593259,
			-0.42500350670542297,
			-1.8685384549837945,
			0.44775007313519744,
			2.4773366470394707,
			-1.6308724145073934
		],
		[
			-0.13813295696769345,
			0.69434840566213907,
			-0.42498046133534895,
			-1.8863115049043395,
			0.44751967860420022,
			2.485938413755151,
			-1.6218809603886475
		],
		[
			-0.12426390989104937,
			0.68465559854978608,
			-0.42492239646754515,
			-1.9040608177414469,
			0.44724012648748412,
			2.4945540766885408,
			-1.6123999087715537
		],
		[
			-0.11003029138838329,
			0.67496628659269919,
			-0.4248265329778349,
			-1.9217583835110035,
			0.44690852289468336,
			2.5031703601206861,
			-1.6024122925947875
		],
		[
			-0.095428368026116817,
			0.66529575080211367,
			-0.42468999253851336,
			-1.9393755988446966,
			0.44652194820333491,
			2.5117735731098367,
			-1.5919010661764659
		],
		[
			-0.080454357113822095,
			0.65565975933827669,
			-0.42450979751180884,
			-1.9568831894387297,
			0.44607746637026224,
			2.5203495690684368,
			-1.5808491655644041
		],
		[
			-0.065104483790737341,
			0.64607461371743058,
			-0.42428287183285862,
			-1.9742511315236468,
			0.44557213607922647,
			2.5288837053135174,
			-1.5692395787785476
		],
		[
			-0.049375045460687828,
			0.63655719471781469,
			-0.42400604306642176,
			-1.9914485729226008,
			0.44500302388367102,
			2.5373608029620174,
			-1.5570554268503818
		],
		[
			-0.033262484152383281,
			0.62712500753319111,
			-0.42367604584268637,
			-2.0084437543264522,
			0.44436721949120456,
			2.5457651075838785,
			-1.5442800565396257
		],
		[
			-0.016763467360596186,
			0.61779622567089232,
			-0.42328952689961136,
			-2.0252039314879844,
			0.44366185331679509,
			2.5540802510724143,
			-1.5308971455560108
		],
		[
			0.00012502212209667511,
			0.60858973303448338,
			-0.42284305198162997,
			-2.0416952991232162,
			0.44288411640283198,
			2.5622892152423935,
			-1.516890821026506
		],
		[
			0.017405586948600026,
			0.59952516357010199,
			-0.42233311486639646,
			-2.057882917403715,
			0.44203128276440284,
			2.5703742977203063,
			-1.5022457918182706
		],
		[
			0.035080306211125206,
			0.59062293779229624,
			-0.42175614881125439,
			-2.073730642027602,
			0.44110073416562379,
			2.5783170807466784,
			-1.4869474951468844
		],
		[
			0.053150616511014333,
			0.58190429544210631,
			-0.4211085407276291,
			-2.0892010589652563,
			0.44008998726595605,
			2.5860984035647663,
			-1.4709822576596614
		],
		[
			0.071617183125046183,
			0.57339132347033661,
			-0.42038664840237577,
			-2.1042554250842054,
			0.43899672299282716,
			2.59369833912077,
			-1.4543374708771508
		],
		[
			0.090479761533135084,
			0.56510697848624702,
			-0.41958682108749579,
			-2.1188536159606404,
			0.43781881789777921,
			2.6010961758443298,
			-1.4370017804952095
		],
		[
			0.10973704986924251,
			0.55707510277096439,
			-0.41870542377013292,
			-2.1329540822752802,
			0.43655437713786566,
			2.6082704053103938,
			-1.4189652885899366
		],
		[
			0.12938653320780799,
			0.5493204329312078,
			-0.41773886540932603,
			-2.1465138162601827,
			0.4352017685933664,
			2.6151987165997146,
			-1.4002197672257384
		],
		[
			0.14942432100044145,
			0.54186860026878947,
			-0.41668363137991055,
			-2.1594883297003169,
			0.43375965748995188,
			2.6218579981698187,
			-1.3807588813442118
		],
		[
			0.16984497942682691,
			0.53474612197180305,
			-0.41553632029213489,
			-2.1718316449872832,
			0.4322270407428872,
			2.6282243480151313,
			-1.3605784181149061
		],
		[
			0.19064136091012168,
			0.52798038230207678,
			-0.41429368525259092,
			-2.1834963006592032,
			0.4306032800897725,
			2.6342730928277351,
			-1.3396765191715883
		],
		[
			0.21180443355590842,
			0.5215996030681892,
			-0.41295267949295106,
			-2.1944333727262522,
			0.42888813293595657,
			2.6399788167623504,
			-1.3180539113603089
		],
		[
			0.23332311378455295,
			0.51563280284178281,
			-0.41151050611362305,
			-2.2045925128607506,
			0.4270817797148474,
			2.6453154002543542,
			-1.2957141308181475
		],
		[
			0.25518410591344826,
			0.51010974460420966,
			-0.40996467146742754,
			-2.2139220042098073,
			0.42518484647753152,
			2.6502560691323849,
			-1.2726637344230132
		],
		[
			0.27737175287651777,
			0.50506087180626735,
			-0.40831304144439112,
			-2.2223688351542927,
			0.4231984213871699,
			2.6547734540030987,
			-1.2489124919532177
		],
		[
			0.29986790260746871,
			0.50051723318956343,
			-0.40655389961737792,
			-2.2298787907801905,
			0.4211240638183027,
			2.6588396595625849,
			-1.2244735517263055
		],
		[
			0.32265179482203332,
			0.49651039715468182,
			-0.40468600587948977,
			-2.2363965611408125,
			0.41896380486239732,
			2.6624263431069695,
			-1.1993635721103637
		],
		[
			0.34569997297414123,
			0.49307235696584883,
			-0.40270865386424054,
			-2.2418658645704399,
			0.41672013822772508,
			2.6655048010771187,
			-1.1736028111794568
		],
		[
			0.36898622599617525,
			0.49023542864722591,
			-0.40062172511151828,
			-2.2462295833673616,
			0.41439600079682209,
			2.668046061985788,
			-1.1472151669754249
		],
		[
			0.39248156403550216,
			0.4880321440409488,
			-0.39842573765578132,
			-2.24942990811053,
			0.41199474246315021,
			2.6700209835504225,
			-1.120228161388376
		],
		[
			0.41615423175047001,
			0.48649514214582751,
			-0.39612188650253144,
			-2.2514084857298764,
			0.40952008529500272,
			2.6714003513046665,
			-1.0926728616077017
		],
		[
			0.43996976182500097,
			0.48565706251935664,
			-0.39371207336178587,
			-2.2521065652431527,
			0.40697607254420282,
			2.6721549754027194,
			-1.0645837344309592
		],
		[
			0.46389107021442966,
			0.48555044518335538,
			-0.39119892305833925,
			-2.2514651338340652,
			0.40436700849548524,
			2.6722557817803119,
			-1.0359984304267491
		],
		[
			0.4878785932762984,
			0.48620764210474215,
			-0.38858578426638679,
			-2.2494250347102041,
			0.40169739059916987,
			2.6716738933109228,
			-1.0069574969750652
		],
		[
			0.51189046541522532,
			0.48766074591056413,
			-0.38587671263634837,
			-2.2459270569740273,
			0.39897183570217348,
			2.6703806961092957,
			-0.97750402146696469
		],
		[
			0.53588273424122956,
			0.4899415420305786,
			-0.38307643499238742,
			-2.2409119865844769,
			0.39619500245126354,
			2.6683478856934406,
			-0.9476832083179848
		],
		[
			0.560145881506244,
			0.49238217574137966,
			-0.38063920269529511,
			-2.2345052169388619,
			0.39289219330305164,
			2.6650440249221057,
			-0.9172075862170912
		],
		[
			0.58548118969463003,
			0.49300934515668104,
			-0.3798063396444249,
			-2.227189906838984,
			0.38774466412646624,
			2.6590134840756434,
			-0.88528742241847125
		],
		[
			0.61073332490853294,
			0.49324141398947374,
			-0.37958043198555391,
			-2.218658659663344,
			0.38182396404463559,
			2.6513535841872571,
			-0.85310542038507065
		],
		[
			0.63530439828491347,
			0.49436055493793146,
			-0.379113297380963,
			-2.2085578059047588,
			0.37600175397284286,
			2.6429814097596429,
			-0.82122510703473051
		],
		[
			0.65916301958471679,
			0.49637465272087833,
			-0.37840201066929929,
			-2.1968890584925855,
			0.37030679337108102,
			2.6339070408507781,
			-0.78970043928032552
		],
		[
			0.68228295124652549,
			0.4992907993700888,
			-0.37744727866041933,
			-2.1836541426856457,
			0.36476403829268023,
			2.6241401140909733,
			-0.75857913174438063
		],
		[
			0.70464287798334047,
			0.50311540267561472,
			-0.37625315415928201,
			-2.1688543974792314,
			0.35939443058692616,
			2.6136895759812657,
			-0.72790239404202817
		]
	]

test2 = []
for point in test:
    test2.extend(point)


def trajectory_safety_check_client(t):
    rospy.wait_for_service('/panda/trajectory_safety_check')
    try:
        local_trajectory_safety_check = rospy.ServiceProxy('/panda/trajectory_safety_check', trajectory_safety_check)
        res = local_trajectory_safety_check(t)
        return res
        # return res.is_safe
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)


def check(trajectory, execution_time):
    # rospy.wait_for_service('/panda/trajectory_safety_check')
    try:
        local_trajectory_safety_check = rospy.ServiceProxy('/panda/trajectory_safety_check', trajectory_safety_check)
        res = local_trajectory_safety_check(trajectory, execution_time)
        return res
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def get_z_bounds():
    # rospy.wait_for_service('/panda/trajectory_safety_check')
    try:
        local_get_z_bounds = rospy.ServiceProxy('/panda/trajectory_safety_check_z_getter', trajectory_safety_check_z_getter)
        res = local_get_z_bounds()
        return res.z_lower, res.z_upper
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def get_y_bounds():
    # rospy.wait_for_service('/panda/trajectory_safety_check')
    try:
        local_get_y_bounds = rospy.ServiceProxy('/panda/trajectory_safety_check_y_getter', trajectory_safety_check_y_getter)
        res = local_get_y_bounds()
        return res.y_lower, res.y_upper
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

if __name__ == "__main__":
    print ("Requesting safety check.")
    print ("Safety check result: %s"%(trajectory_safety_check_client(test2)))
    print ("Safety check request ended.")
