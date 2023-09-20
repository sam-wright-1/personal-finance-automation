drop table if exists public.categories;

create table public.categories
as
SELECT 
  master.type
  , master.date
  , master.amount
  , master.description
  , master.individual
  , master.month
  , master.year
  , master.day
  , master.flow

, CASE
    WHEN UPPER(master.description) LIKE '%AWS.AMAZON.CO%' 
            OR UPPER(master.description) LIKE '%SPOTIFY%' 
            OR UPPER(master.description) LIKE '%PRIME VIDEO%'
            OR UPPER(master.description) LIKE '%APPLE.COM/BILL%'
            OR UPPER(master.description) LIKE '%PRIME VIDEO%'
            OR (UPPER(master.description) LIKE '%GOOGLE%' AND UPPER(master.description) NOT LIKE '%FIBER%')
    THEN 'Software Services'
    WHEN UPPER(master.description) LIKE '%VENMO%'
            OR UPPER(master.description) LIKE '%APPLE CASH%'  
    THEN 'Cash Apps'
    WHEN UPPER(master.description) LIKE '%QUESTAR%'
            OR UPPER(master.description) LIKE '%NESTEGG%'
            OR UPPER(master.description) LIKE '%ZELLE%'
    THEN 'Utilities'
    WHEN UPPER(master.description) LIKE '%FIBER%'
            OR UPPER(master.description) LIKE '%INTERNET%'
    THEN 'Internet/Cell Services'
    WHEN UPPER(master.description) LIKE '%ONLINE TRANSFER%'
            OR UPPER(master.description) LIKE '%DEPOSIT%'
            OR UPPER(master.description) LIKE '%TAX%'
            OR UPPER(master.description) LIKE '%REIMBURSED%'
            OR UPPER(master.description) LIKE '%WITHDRAWAL%'
            OR UPPER(master.description) LIKE '%ONLINE PAYMENT%'
            OR UPPER(master.description) LIKE '%PAYMENT THANK YOU%'
            OR UPPER(master.description) LIKE '%AUTOPAY%'
            OR UPPER(master.description) LIKE '%INTEREST PAYMENT%'
            OR UPPER(master.description) LIKE '%TPG PRODUCTS%'
            OR UPPER(master.description) LIKE '%ATM TRANSACTION%'
    THEN 'Transfers'
    WHEN UPPER(master.description) LIKE '%COSTCO WHSE%'
            OR UPPER(master.description) LIKE '%MACEYS%'
            OR UPPER(master.description) LIKE '%SMITHS%'
            OR UPPER(master.description) LIKE '%WALMART%'
            OR UPPER(master.description) LIKE '%WAL-MART%'
            OR UPPER(master.description) LIKE '%HARMONS%'
            OR UPPER(master.description) LIKE '%TIME TRAVELER%'
            OR UPPER(master.description) LIKE '%SUPERCENTER%'
            OR UPPER(master.description) LIKE '%COSTCO CASH REWARD%'
            OR UPPER(master.description) LIKE '%COSTCO ANNUAL MEMBERSHIP%'
            OR UPPER(master.description) LIKE '%SAFEWAY%'
            OR UPPER(master.description) LIKE '%CIRCLE K%'
    THEN 'Groceries'
    WHEN UPPER(master.description) LIKE '%CHICK-FIL-A%'
            OR UPPER(master.description) LIKE '%CRUMBL%'
            OR UPPER(master.description) LIKE '%TAMASHI%'
            OR UPPER(master.description) LIKE '%FILLINGS & EMULSIONS%'
            OR UPPER(master.description) LIKE '%WENDYS%'
            OR UPPER(master.description) LIKE '%CARLS%'
            OR UPPER(master.description) LIKE '%CHOM%'
            OR UPPER(master.description) LIKE '%STREET TACOS%'
            OR UPPER(master.description) LIKE '%CAFE TRANG%'
            OR UPPER(master.description) LIKE '%PANDA%'
            OR UPPER(master.description) LIKE '%KNEADERS%'
            OR UPPER(master.description) LIKE '%PANERA%'
            OR UPPER(master.description) LIKE '%JCW%'
            OR UPPER(master.description) LIKE '%COSTA%'
            OR UPPER(master.description) LIKE '%CUBBYS%'
            OR UPPER(master.description) LIKE '%MCDONALDS%'
            OR UPPER(master.description) LIKE '%MCDONALD''S%'
            OR UPPER(master.description) LIKE '%IN N OUT%'
            OR UPPER(master.description) LIKE '%PHO PLUS%'
            OR UPPER(master.description) LIKE '%SWIG%'
            OR UPPER(master.description) LIKE '%PHO THIN%'
            OR UPPER(master.description) LIKE '%SONIC%'
            OR UPPER(master.description) LIKE '%SUPERFOODS%'
            OR UPPER(master.description) LIKE '%MORNING SQUEEZE%'
            OR UPPER(master.description) LIKE '%CAFE%'
            OR UPPER(master.description) LIKE '%JIMMY JOHNS%'
            OR UPPER(master.description) LIKE '%TEXAS ROADHOUSE%'
            OR UPPER(master.description) LIKE '%BEANS AND BREWS%'
            OR UPPER(master.description) LIKE '%TACOS%'
            OR UPPER(master.description) LIKE '%PAPA%'
            OR UPPER(master.description) LIKE '%ROXBERRY%'
            OR UPPER(master.description) LIKE '%MELTING POT%'
            OR UPPER(master.description) LIKE '%BERRY DIVINE%'
            OR UPPER(master.description) LIKE '%5GUYS%'
            OR UPPER(master.description) LIKE '%FIVE GUYS%'
            OR UPPER(master.description) LIKE '%STARBUCKS%'
            OR UPPER(master.description) LIKE '%RED ROBIN%'
            OR UPPER(master.description) LIKE '%CHIPOTLE%'
            OR UPPER(master.description) LIKE '%ALOHA KITCHEN%'
            OR UPPER(master.description) LIKE '%FIREHOUSE%'
            OR UPPER(master.description) LIKE '%TWO JACKS%'
            OR UPPER(master.description) LIKE '%ITALIAN%'
            OR UPPER(master.description) LIKE '%PIZZA%'
            OR UPPER(master.description) LIKE '%FOOD%'
            OR UPPER(master.description) LIKE '%BBQ%'
            OR UPPER(master.description) LIKE '%EATERY%'
            OR UPPER(master.description) LIKE '%BAKERY%'
            OR UPPER(master.description) LIKE '%GRILL%'
            OR UPPER(master.description) LIKE '%BREW%'
            OR UPPER(master.description) LIKE '%SLAPFISH%'
            OR UPPER(master.description) LIKE '%BOWL%'
            OR UPPER(master.description) LIKE '%TRADER JOE%'
            OR UPPER(master.description) LIKE '%CREAMERY%'
            OR UPPER(master.description) LIKE '%BIRDHOUSE%'
            OR UPPER(master.description) LIKE '%BURGER%'
            OR UPPER(master.description) LIKE '%DONUTS%'
            OR UPPER(master.description) LIKE '%THAI%'
            OR UPPER(master.description) LIKE '%SUB ZERO%'
            OR UPPER(master.description) LIKE '%KITCHE%'
            OR UPPER(master.description) LIKE '%ICE CREAM%'
            OR UPPER(master.description) LIKE '%BISTRO%'
            OR UPPER(master.description) LIKE '%EINSTEIN BAGELS%'
            OR UPPER(master.description) LIKE '%CHEESECAKE%'
            OR UPPER(master.description) LIKE '%TAQUERIA%'
            OR UPPER(master.description) LIKE '%JAMBA JUICE%'
            OR UPPER(master.description) LIKE '%BB DINER%'
            OR UPPER(master.description) LIKE '%LUNCHBOX%'
            OR UPPER(master.description) LIKE '%HARWARD FARMS SWEET%'
    THEN 'Fast Food'
    WHEN UPPER(master.description) LIKE '%COSTCO GAS%'
            OR UPPER(master.description) LIKE '%MAVERIK%'
            OR UPPER(master.description) LIKE '%FLYING J%'
            OR UPPER(master.description) LIKE '%CHEVRON%'
            OR UPPER(master.description) LIKE '%7-ELEVEN%'
    THEN 'Gas'
    WHEN UPPER(master.description) LIKE '%ULTA%'
            OR UPPER(master.description) LIKE '%ETSY%'
            OR UPPER(master.description) LIKE '%HOME DEPOT%'
            OR UPPER(master.description) LIKE '%BATH & BODY%'
            OR UPPER(master.description) LIKE '%BARNES & NOBLE%'
            OR UPPER(master.description) LIKE '%ACE%'
            OR UPPER(master.description) LIKE '%TAILOR%'
            OR UPPER(master.description) LIKE '%READY GUNNER%'
            OR UPPER(master.description) LIKE '%LOWES%'
            OR UPPER(master.description) LIKE '%IKEA%'
            OR UPPER(master.description) LIKE '%JOANN%'
            OR UPPER(master.description) LIKE '%FORGE JEWELRY%'
            OR UPPER(master.description) LIKE '%BEAUTY BY EARTH%'
            OR UPPER(master.description) LIKE '%APPLE STORE%'
            OR UPPER(master.description) LIKE '%AL\''S%'
            OR UPPER(master.description) LIKE '%ZURCHERS%'
            OR UPPER(master.description) LIKE '%LEGO%'
            OR UPPER(master.description) LIKE '%BABY%'
            OR UPPER(master.description) LIKE '%HOME STORE%'
            OR UPPER(master.description) LIKE '%HOBBY%'
            OR UPPER(master.description) LIKE '%MICHAELS%'
            OR UPPER(master.description) LIKE '%HOMEGOODS%'
            OR UPPER(master.description) LIKE '%BOUTIQUE%'
            OR UPPER(master.description) LIKE '%GUNNIES%'
            OR UPPER(master.description) LIKE '%WICK LAB%'
            OR UPPER(master.description) LIKE '%BOOK%'
            OR UPPER(master.description) LIKE '%TOP GOLF%'
            OR UPPER(master.description) LIKE '%STUBHUB%'
            OR UPPER(master.description) LIKE '%FEDEX%'
            OR UPPER(master.description) LIKE '%USPS%'
            OR UPPER(master.description) LIKE '%HALLOWEEN%'
            OR UPPER(master.description) LIKE '%NZXT%'
            OR UPPER(master.description) LIKE '%STAPLES%'
            OR UPPER(master.description) LIKE '%SALT LAKE BEES%'
            OR UPPER(master.description) LIKE '%HUNT/FISH%'
            OR UPPER(master.description) LIKE '%REPOTME%'
            OR UPPER(master.description) LIKE '%TICKETS%'
            OR UPPER(master.description) LIKE '%GOFUNDME%'
            OR UPPER(master.description) LIKE '%CHARITY%'
            OR UPPER(master.description) LIKE '%SILVER SAFARI%'
            OR UPPER(master.description) LIKE '%SP STANLEY%'
            OR UPPER(master.description) LIKE '%SUN RIVER GARDENS%'
            OR UPPER(master.description) LIKE '%BEANYS TO GO VINEYARD%'
            OR UPPER(master.description) LIKE '%LDS DIST ONLINE%'
            OR UPPER(master.description) LIKE '%CCRI BY U%'
            OR UPPER(master.description) LIKE '%UTAHDHA%'
            OR UPPER(master.description) LIKE '%BOYCHIK%'
            OR UPPER(master.description) LIKE '%SUNOCO%'
            OR UPPER(master.description) LIKE '%CINEMARK%'
            OR UPPER(master.description) LIKE '%UNIVERSITY MALL%'
            OR UPPER(master.description) LIKE '%SEINT 801%'
            OR UPPER(master.description) LIKE '%VIVID SEATS%'
            OR UPPER(master.description) LIKE '%THE KINLANDS%'
            OR UPPER(master.description) LIKE '%CUDDLES RESCUE%'
            OR UPPER(master.description) LIKE '%NATIONAL DME%'
            OR UPPER(master.description) LIKE '%WICKED CUSHIONS%'
            OR UPPER(master.description) LIKE '%DOLLAR TREE%'
            OR UPPER(master.description) LIKE '%06/24 DSW%'
            OR UPPER(master.description) LIKE '%SMITHBALLPARK%'
            OR UPPER(master.description) LIKE '%TICKETMASTER%'
            OR UPPER(master.description) LIKE '%OREM SUMMER SN OREM%'
            OR UPPER(master.description) LIKE '%SALT LAKE CITY DEP SALT LAKE%'
            OR UPPER(master.description) LIKE '%HOGLE ZOO SALT LAKE%'
    THEN 'Miscellaneous'
    WHEN UPPER(master.description) LIKE '%QUICKQUACK%'
            OR UPPER(master.description) LIKE '%AUTO PARTS%'
            OR UPPER(master.description) LIKE '%AUTOZONE%'
            OR UPPER(master.description) LIKE '%JIFFY LUBE%'
            OR UPPER(master.description) LIKE '%O\''REILLY%'
            OR UPPER(master.description) LIKE '%DMV%'
            OR UPPER(master.description) LIKE '%LES SCHWAB%'
            OR UPPER(master.description) LIKE '%CLEGG AUTO%'
            OR UPPER(master.description) LIKE '%DMV%'
            OR UPPER(master.description) LIKE '%DRIVER%'
            OR UPPER(master.description) LIKE '%PARKING%'
            OR UPPER(master.description) LIKE '%AUTOGLASS%'
            OR UPPER(master.description) LIKE '%CAR WASH%'
    THEN 'Cars'
    WHEN UPPER(master.description) LIKE '%TARGET%'
            OR UPPER(master.description) LIKE '%NIKE%'
            OR UPPER(master.description) LIKE '%AMERICAN EAGLE%'
            OR UPPER(master.description) LIKE '%TARGET%'
            OR UPPER(master.description) LIKE '%NORDRACK%'
            OR UPPER(master.description) LIKE '%COLEHAAN%'
            OR UPPER(master.description) LIKE '%BUCKLE%'
            OR UPPER(master.description) LIKE '%AE OUT%'
            OR UPPER(master.description) LIKE '%COTTON ON%'
            OR UPPER(master.description) LIKE '%ALBION%'
            OR UPPER(master.description) LIKE '%GAP%'
            OR UPPER(master.description) LIKE '%BOHME%'
            OR UPPER(master.description) LIKE '%SEPHORA%'
            OR UPPER(master.description) LIKE '%H&M%'
            OR UPPER(master.description) LIKE '%TIMBERLAND%'
            OR UPPER(master.description) LIKE '%BYLT%'
            OR UPPER(master.description) LIKE '%NORDSTROM%'
            OR UPPER(master.description) LIKE '%KIZIK%'
            OR UPPER(master.description) LIKE '%BRONXTON%'
            OR UPPER(master.description) LIKE '%QUIKSILVER%'
            OR UPPER(master.description) LIKE '%ADIDAS%'
            OR UPPER(master.description) LIKE '%QUIKSILVER%'
            OR UPPER(master.description) LIKE '%DOWNEAST%'
            OR UPPER(master.description) LIKE '%VANS%'
            OR UPPER(master.description) LIKE '%OLD NAVY%'
            OR UPPER(master.description) LIKE '%CLAIRE%'
            OR UPPER(master.description) LIKE '%COLE HAAN%'
            OR UPPER(master.description) LIKE '%LULULEMON%'
            OR UPPER(master.description) LIKE '%SHOP STEVIE%'
            OR UPPER(master.description) LIKE '%LOVE OLIVE CO%'
            OR UPPER(master.description) LIKE '%UPTOWN CHEAPSKATE%'
            OR UPPER(master.description) LIKE '%LIVY&KATE%'
            OR UPPER(master.description) LIKE '%CLOTHIN%'
            OR UPPER(master.description) LIKE '%MENTIONABLES%'
            OR UPPER(master.description) LIKE '%UNDER ARMOUR%'
            OR UPPER(master.description) LIKE '%BARBELL%'
            OR UPPER(master.description) LIKE '%FACTORY OUTLET%'
            OR UPPER(master.description) LIKE '%MIKAROSE%'
            OR UPPER(master.description) LIKE '%CONVERSE%'
            OR UPPER(master.description) LIKE '%BRAXLEY BANDS%'
            OR UPPER(master.description) LIKE '%HALFTEES%'
            OR UPPER(master.description) LIKE '%LENIN RM LLC%'
            OR UPPER(master.description) LIKE '%PUBLIX%'
            OR UPPER(master.description) LIKE '%MADEBYMARY%'
            OR UPPER(master.description) LIKE '%THE SOCK DRAWER%'
    THEN 'Clothes'
    WHEN UPPER(master.description) LIKE '%COLLEGE%'
            OR UPPER(master.description) LIKE '%STUDENT%'
            OR UPPER(master.description) LIKE '%UDEMY%'
            OR UPPER(master.description) LIKE '%CHECK #%'
            OR UPPER(master.description) LIKE '%WESTERN REGIONAL EXAM%'
            OR UPPER(master.description) LIKE '%PREP BLAST%'
    THEN 'School'
    WHEN UPPER(master.description) LIKE '%AMERICAN AIR%'
            OR UPPER(master.description) LIKE '%VRBO%'  
            OR UPPER(master.description) LIKE '%DELTA%'  
            OR UPPER(master.description) LIKE '%HERTZ%'  
            OR UPPER(master.description) LIKE '%HOTEL%'  
            OR UPPER(master.description) LIKE '%ROYAL CARIBBEAN%'  
            OR UPPER(master.description) LIKE '%SEAS%'  
            OR UPPER(master.description) LIKE '%UBER%'  
            OR UPPER(master.description) LIKE '%AIRBNB%'  
            OR UPPER(master.description) LIKE '%VACATION%'  
            OR UPPER(master.description) LIKE '%INN%' 
            OR UPPER(master.description) LIKE '%ALASKA%' 
            OR UPPER(master.description) LIKE '%AIRPORT%' 
            OR UPPER(master.description) LIKE '%ATLANTA%'
            OR UPPER(master.description) LIKE '%SAVANNAH%'
            OR UPPER(master.description) LIKE '%MARRIOTT%'
            OR UPPER(master.description) LIKE '%CHARLESTON%'
            OR UPPER(master.description) LIKE '%TYBEE ISLAND%'
            OR UPPER(master.description) LIKE '%ISLE OF PALMS%'
            OR UPPER(master.description) LIKE '%SOUTHWES%'
            OR (UPPER(master.description) LIKE '%RENT%' AND UPPER(master.description) LIKE '%CAR%')
    THEN 'Travel'
    WHEN UPPER(master.description) LIKE '%PROVO SPORTS%'
            OR UPPER(master.description) LIKE '%WALGREENS%'
            OR UPPER(master.description) LIKE '%REVEREHEALTH%'
            OR UPPER(master.description) LIKE '%HUNNY B%'
            OR UPPER(master.description) LIKE '%SALON%'
            OR UPPER(master.description) LIKE '%OLAPLEX%'
            OR UPPER(master.description) LIKE '%HUNNY B%'
            OR UPPER(master.description) LIKE '%HAIR%'
            OR UPPER(master.description) LIKE '%UVEC - CONTACTS%'
            OR UPPER(master.description) LIKE '%PHARMACY%'
            OR UPPER(master.description) LIKE '%CVS%'
            OR UPPER(master.description) LIKE '%MEDIC%'
            OR UPPER(master.description) LIKE '%BEAUTY%'
            OR UPPER(master.description) LIKE '%PROVO REC%'
            OR UPPER(master.description) LIKE '%UVEC%'
            OR UPPER(master.description) LIKE '%CHIRO%'
            OR UPPER(master.description) LIKE '%EYE%'
            OR UPPER(master.description) LIKE '%INTERMOUNTAIN%'
            OR UPPER(master.description) LIKE '%HYPERICE%'
            OR UPPER(master.description) LIKE '%SKINCARE%'
            OR UPPER(master.description) LIKE '%ROSENBERG COOLEY%'
            OR UPPER(master.description) LIKE '%INSTACARE%'
            OR UPPER(master.description) LIKE '%NAILS%'
            OR UPPER(master.description) LIKE '%PAUL MITCHELL%'
            OR UPPER(master.description) LIKE '%LOREAL%'
    THEN 'Health'
    WHEN UPPER(master.description) LIKE '%.COM%'
            OR UPPER(master.description) LIKE '%AMZN%'  
            OR UPPER(master.description) LIKE '%COSTCO COM%'  
    THEN 'Web Purchase'
    WHEN UPPER(master.description) LIKE 'ONLINE PAYMENT, THANK YOU%'
            OR UPPER(master.description) LIKE 'CITI CARD ONLINE PAYMENT%'
            OR UPPER(master.description) LIKE 'CITI AUTOPAY PAYMENT%'
            OR UPPER(master.description) LIKE 'ONLINE TRANSFER TO WRIGHT%'
            OR UPPER(master.description) LIKE 'ONLINE TRANSFER FROM WRIGHT%'
            OR UPPER(master.description) LIKE 'AUTOPAY 211%'
            OR UPPER(master.description) LIKE 'PAYMENT THANK YOU%'
    THEN 'Credit Card Payments'
    ELSE 'Unknown'
  END AS transaction_category

FROM public.master_join as master -- This is uploaded
;