// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-collection",
          title: "Collection",
          description: "Browse the complete Fall of the Republic Collection",
          section: "Navigation",
          handler: () => {
            window.location.href = "/collection/";
          },
        },{id: "nav-books",
          title: "Books",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/books/";
          },
        },{id: "books-historia-numorum-italy",
          title: 'Historia numorum--Italy',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/author_historia_numorum_italy/";
            },},{id: "books-the-landmark-julius-caesar-the-complete-works",
          title: 'The Landmark Julius Caesar : The Complete Works',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/author_the_landmark_julius_caesar_t/";
            },},{id: "books-emperor-of-rome",
          title: 'Emperor of Rome',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/beard_emperor_of_rome/";
            },},{id: "books-rome-in-the-late-republic",
          title: 'Rome in the late Republic',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/beard_rome_in_the_late_republic/";
            },},{id: "books-the-fires-of-vesuvius",
          title: 'The fires of Vesuvius',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/beard_the_fires_of_vesuvius/";
            },},{id: "books-twelve-caesars",
          title: 'Twelve Caesars',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/beard_twelve_caesars/";
            },},{id: "books-100-greatest-ancient-coins",
          title: '100 Greatest Ancient Coins',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/berk_100_greatest_ancient_coins/";
            },},{id: "books-the-magistrates-of-the-roman-republic",
          title: 'The Magistrates of the Roman Republic',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/broughton_magistrates_roman_republic/";
            },},{id: "books-the-roman-provinces-300-bce-300-ce-using-coins-as-sources",
          title: 'The Roman Provinces, 300 BCE-300 CE Using Coins as Sources',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/burnett_the_roman_provinces_300_bce_3/";
            },},{id: "books-roman-republican-coinage",
          title: 'Roman Republican Coinage',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/crawford_roman_republican_coinage/";
            },},{id: "books-the-roman-republic",
          title: 'The Roman Republic',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/crawford_the_roman_republic_fontana_hi/";
            },},{id: "books-cambridge-companion-to-the-roman-republic",
          title: 'Cambridge Companion to the Roman Republic',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/flower_cambridge_companion_to_the_rom/";
            },},{id: "books-roman-republics",
          title: 'Roman Republics',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/flower_roman_republics/";
            },},{id: "books-the-encyclopedia-of-the-roman-empire",
          title: 'The Encyclopedia of the Roman Empire',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/gomez_encyclopedia_roman_empire/";
            },},{id: "books-moneta-a-brief-history-of-ancient-rome-in-twelve-coins",
          title: 'Moneta: A Brief History of Ancient Rome in Twelve Coins',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/harney_moneta/";
            },},{id: "books-guide-to-biblical-coins",
          title: 'Guide to Biblical coins',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/hendin_guide_to_biblical_coins/";
            },},{id: "books-athenian-empire-using-coins-as-sources",
          title: 'Athenian Empire: Using Coins as Sources',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/kallet_athenian_empire/";
            },},{id: "books-archaic-and-classical-greek-coins",
          title: 'Archaic and classical Greek coins',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/kraay_archaic_and_classical_greek_co/";
            },},{id: "books-unruly",
          title: 'Unruly',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/mitchell_unruly/";
            },},{id: "books-coins-of-the-roman-republic-in-the-british-museum",
          title: 'Coins of the Roman Republic in the British Museum',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/museum_coins_of_the_roman_republic_in/";
            },},{id: "books-your-cheeky-guide-to-the-roman-empire",
          title: 'Your Cheeky Guide to the Roman Empire',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/radford_your_cheeky_guide_to_the_roman/";
            },},{id: "books-companion-to-the-roman-republic",
          title: 'Companion to the Roman Republic',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/rosenstein_companion_to_the_roman_republi/";
            },},{id: "books-from-caesar-to-augustus",
          title: 'From Caesar to Augustus',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/rowan_from_caesar_to_augustus/";
            },},{id: "books-insane-emperors-sunken-cities-and-earthquake-machines",
          title: 'Insane Emperors, Sunken Cities, and Earthquake Machines',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/ryan_insane_emperors_sunken_cities/";
            },},{id: "books-naked-statues-fat-gladiators-and-war-elephants",
          title: 'Naked Statues, Fat Gladiators, and War Elephants',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/ryan_naked_statues_fat_gladiators/";
            },},{id: "books-from-the-gracchi-to-nero",
          title: 'From the Gracchi to Nero',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/scullard_from_gracchi_to_nero/";
            },},{id: "books-history-and-coinage-of-the-roman-imperators-49-27-bc",
          title: 'History and Coinage of the Roman Imperators 49-27 BC',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/sear_history_and_coinage_of_the_rom/";
            },},{id: "books-spqr-a-history-of-ancient-rome",
          title: 'SPQR: A History of Ancient Rome',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/spqr_mary_beard/";
            },},{id: "books-the-storm-before-the-storm-the-beginning-of-the-end-of-the-roman-republic",
          title: 'The Storm Before the Storm: The Beginning of the End of the Roman...',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/storm_before_storm/";
            },},{id: "books-roman-imperial-coinage",
          title: 'Roman Imperial Coinage',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/sutherland_roman_imperial_coinage/";
            },},{id: "books-the-roman-revolution",
          title: 'The Roman Revolution',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/syme_the_roman_revolution/";
            },},{id: "books-hellenistic-world-using-coins-as-sources",
          title: 'Hellenistic World: : Using Coins as Sources',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/thonemann_hellenistic_world/";
            },},{id: "books-palatine-the-four-emperors-series",
          title: 'Palatine : The Four Emperors Series',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/trafford_palatine_the_four_emperors_s/";
            },},{id: "books-the-rbw-collection-of-roman-republican-coins",
          title: 'The RBW Collection of Roman Republican Coins',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/vagi_the_rbw_collection_of_roman_re/";
            },},{id: "books-italian-cast-coinage-a-descriptive-catalogue-of-the-cast-bronze-coinage-and-its-struck-counterparts-in-ancient-italy-from-the-7th-to-3rd-centuries-bc",
          title: 'Italian Cast Coinage A Descriptive Catalogue of the Cast Bronze Coinage and Its...',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/vecchi_italian_cast_coinage_a_descrip/";
            },},{id: "books-the-fall-of-rome",
          title: 'The Fall of Rome',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/ward_perkins_the_fall_of_rome/";
            },},{id: "books-roman-republic-to-49-bce-using-coins-as-sources",
          title: 'Roman Republic to 49 BCE: Using Coins as Sources',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/yarrow_roman_republic_to_49_bce/";
            },},{id: "coins-denarius-of-q-servilius-caepio-and-l-calpurnius-piso",
          title: 'Denarius of Q. Servilius Caepio and L. Calpurnius Piso',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/capio_piso/";
            },},{id: "coins-denarius-of-l-saturnius",
          title: 'Denarius of L. Saturnius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/saturnius/";
            },},{id: "coins-denarius-of-trajan",
          title: 'Denarius of Trajan',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/trajan/";
            },},{id: "coins-denarius-of-p-porcius-laeca",
          title: 'Denarius of P. Porcius Laeca',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/p_porcius_laeca/";
            },},{id: "coins-denarius-of-p-licinius-nerva",
          title: 'Denarius of P. Licinius Nerva',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/p_licinius_nerva/";
            },},{id: "coins-denarius-of-c-cassius",
          title: 'Denarius of C. Cassius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/c_cassius/";
            },},{id: "coins-denarius-of-l-opimius",
          title: 'Denarius of L. Opimius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/l_opimius/";
            },},{id: "coins-denarius-of-hadrian",
          title: 'Denarius of Hadrian',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/hadrian/";
            },},{id: "coins-denarius-of-tiberius",
          title: 'Denarius of Tiberius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/tiberius/";
            },},{id: "coins-denarius-of-antoninus-pius-with-marcus-aurelius-as-caesar",
          title: 'Denarius of Antoninus Pius with Marcus Aurelius as Caesar',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/pius_aurelius/";
            },},{id: "coins-denarius-of-marcus-aurelius",
          title: 'Denarius of Marcus Aurelius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/marcus_aurelius/";
            },},{id: "coins-denarius-of-commodus",
          title: 'Denarius of Commodus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/commodus/";
            },},{id: "coins-anonymous-denarius",
          title: 'Anonymous Denarius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/anonymous_denarius/";
            },},{id: "coins-denarius-of-octavian",
          title: 'Denarius of Octavian',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/octavian_curia_julia/";
            },},{id: "coins-as-of-caligula",
          title: 'As of Caligula',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/caligula/";
            },},{id: "coins-as-of-claudius",
          title: 'As of Claudius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/claudius/";
            },},{id: "coins-denarius-of-t-carisius",
          title: 'Denarius of T. Carisius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/t_carisius/";
            },},{id: "coins-denarius-of-gaius-pansa-and-decimus-brutus",
          title: 'Denarius of Gaius Pansa and Decimus Brutus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/pansa_brutus/";
            },},{id: "coins-denarius-of-q-sicinius",
          title: 'Denarius of Q. Sicinius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/sicinius/";
            },},{id: "coins-denarius-of-m-junius-brutus",
          title: 'Denarius of M. Junius Brutus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/brutus_ahala/";
            },},{id: "coins-denarius-of-faustus-cornelius-sulla",
          title: 'Denarius of Faustus Cornelius Sulla',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/faustus_sulla/";
            },},{id: "coins-denarius-of-faustus-cornelius-sulla",
          title: 'Denarius of Faustus Cornelius Sulla',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/faustus_sulla_signet/";
            },},{id: "coins-denarius-of-l-cassius-longinus",
          title: 'Denarius of L. Cassius Longinus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/cassius_longinus_voting/";
            },},{id: "coins-denarius-of-mn-aquillius",
          title: 'Denarius of Mn. Aquillius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/mn_aquillius/";
            },},{id: "coins-denarius-of-lucius-aemilius-paullus",
          title: 'Denarius of Lucius Aemilius Paullus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/aemilia_denarius/";
            },},{id: "coins-denarius-of-nero",
          title: 'Denarius of Nero',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/nero/";
            },},{id: "coins-denarius-of-vespasian",
          title: 'Denarius of Vespasian',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/vespasian/";
            },},{id: "coins-denarius-of-titus",
          title: 'Denarius of Titus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/titus/";
            },},{id: "coins-denarius-of-l-manlius-torquatus",
          title: 'Denarius of L. Manlius Torquatus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/sulla/";
            },},{id: "coins-denarius-of-l-titurius-l-f-sabinus",
          title: 'Denarius of L. Titurius L.f. Sabinus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/titurius_sabine_women/";
            },},{id: "coins-denarius-of-l-titurius-l-f-sabinus",
          title: 'Denarius of L. Titurius L.f. Sabinus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/titurius_tarpeia/";
            },},{id: "coins-semis-of-augustus",
          title: 'Semis of Augustus',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/augustus_lugdunum/";
            },},{id: "coins-denarius-of-domitian",
          title: 'Denarius of Domitian',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/domitian/";
            },},{id: "coins-denarius-of-nerva",
          title: 'Denarius of Nerva',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/nerva/";
            },},{id: "coins-denarius-of-julius-caesar",
          title: 'Denarius of Julius Caesar',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/julius_caesar/";
            },},{id: "coins-denarius-of-otho",
          title: 'Denarius of Otho',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/otho/";
            },},{id: "coins-denarius-of-galba",
          title: 'Denarius of Galba',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/galba/";
            },},{id: "coins-denarius-of-vitellius",
          title: 'Denarius of Vitellius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/vitellius/";
            },},{id: "coins-denarius-of-m-porcius-cato",
          title: 'Denarius of M. Porcius Cato',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/m_porcius_cato/";
            },},{id: "coins-denarius-of-cn-nerius",
          title: 'Denarius of Cn. Nerius',
          description: "",
          section: "Coins",handler: () => {
              window.location.href = "/coins/neria/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
