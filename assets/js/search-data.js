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
        },{id: "coins-denarius-of-q-servilius-caepio-and-l-calpurnius-piso",
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
