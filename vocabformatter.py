# this script parses each string of vocab words into a dictionary

unit1 = """Innovations
new method, idea, product, etc.
Maize
Corn, first crop farmed in Mexico, helped supply population growth in Old World.
Irrigation
the supply of water to land or crops to help growth, typically by means of channels
Southwestern Indians
Native American peoples inhabiting the southwestern United States
Great Basin
A desert region of the Western United States
Great Plains Indians
Most widespread Indian group in the West, made up of many different tribes and language group, mostly hunted buffalo
Mississippi River Valley Indians
In Eastern Woodlands, was an agricultural society, grew "3 sisters" crops (squash, beans, and corn), were mound builders, Atlantic Seaboard
Atlantic Seaboard
Lived on coastal plains along the Atlantic Coast, used rivers and Atlantic as a source of food and trade, first tribes to meet the British.
Eastern Indians
Small bands of Indians in the northeast region along the Atlantic coast that did not practice intensive agriculture.
Northwestern Indians
Northwestern Indians lived in cool and wet climates such as oceans and forests, with lots of natural resources. They lived in permanent settlements and fished as well as hunting and gathering.
Columbian Exchange
An exchange between the Old World, New World, and Africa. In this exchange the Old World gave the New World food, animals, and diseases. Africa gave the New World slaves.
New World
Americas.
Mercantilism
economic idea that a country's wealth is measured by the amount of gold it owns, economic policy is to export more goods than you import.
Feudalism
Social system that existed in Europe during the Middle Ages in which people worked and fought for nobles who gave them protection and the use of land in return. This system was transferred to the Americas during colonization.
Capitalism
A system of economic production based on the private ownership of property and the contractual exchange for profit of goods, labor, ad money.
Maritime Technology
The Caravel, Compass, Astrolabe, Triangular Arab Sail, Improved maps etc. Impact: Allowed Europeans to navigate easier increasing the travels to the American colonies.
Joint-Stock Companies
A company made up of a group of shareholders. Each shareholder invests some money in the company and, in turn, receives a share of the company's profits.
Epidemics
Diseases brought by Europeans that wiped out a large majority of Indians were smallpox, influenza and measles.
Encomienda System
A labor system instituted by the Spanish crown in the American colonies. In this system, a Spanish encomendero was granted several native laborers who would pay tributes to him in exchange for his protection. (Did not work in the way the crown thought). 
Caste System
A class structure that is determined by birth.
Subjugation
To gain control of, or to conquer. 
Diplomatic
Conduct by government officials of negotiations and other relations between nations.
Pueblo Revolt
A 1680 uprising of the Pueblo Indians against the Spanish who ruled the southwest.
Vallodolid Debates
Concerned the treatment of natives of the New World. It concerned two main attitudes towards the conquest of the Americas. Bartolomé de las Casas argued Amer-Indians were creations of God and deserved same treatment as Christian Europeans. Juan Ginés de Sepúlveda thought that the natives should be slaves because of their crimes against nature and against God."""

title1 = []
definition1 = []

splitted = unit1.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title1.append(z)
        print(z)
    elif i%2 == 0:
        definition1.append(z)

for i in title1:
    if i == '':
        title1.remove(i)
for z in definition1:
    if z == '':
        definition1.remove(z)

content1 = dict(zip(title1, definition1))

unit2 = """Encomiendas
A labor system established by the Spanish Crown in the 1500s. This new system rewarded Spanish explorers, conquistadors, and military men with land in the New World. But they did not just get the land, they got the labor of the people living on the land as well.
Quebec
French colony in North America, with a capital in Quebec, founded 1608.
New Amsterdam
A settlement established by the Dutch near the mouth of Hudson River and the southern end of Manhattan Island.
Social Mobility
The ability of individuals to move from one social standing to another. Social standing is based on degrees of wealth, prestige, education and power.
Benjamin Franklin
American public official, writer, scientist, and printer. After the success of his Poor Richard's Almanac (1732-1757), he entered politics and played a major part in the American Revolution.
Chesapeake Colonies
The region of Virginia and Maryland. In contrast to New England, this region was distinguished by indentured servants, cash crops, and African slavery.
Virginia Company
The first joint-stock company in the colonies; founded Jamestown; promised gold, conversion of Indian to Christianity, and passage to the Indies.
Jamestown
The first successful settlement in the Virginia colony founded in May 1607
House of Burgesses
The first elected general assembly in the colonies, paving the way for the democratic society formed during the Revolution. 
Powhatan
Chief of Algonquian people, a tribe near Jamestown. Tried to make allies with ceremonies, peace charters, corn, trade, etc.
Bacon’s Rebellion
A failed insurrection against the government of colonial Virginia. (Low prices for tobacco, high unjust taxes, land disputes over Native Americans, farmers demanded Powhatan Indians to be removed from their treaty-protected lands)
Indentured Servant
A poor person obligated to a fixed term of unpaid labor, often in exchange for a benefit such as transportation, protection, or training.
Pilgrims
A form of puritans (separatists) who wanted to completely break away from the church of England.
Puritans
Were non-separatists who wished to adopt reforms to purify the Church of England.
Salem Witch Trials
A series of hearings and prosecutions of people accused of witchcraft in colonial Massachusetts between February 1692 and May 1693. The trials resulted in the executions of 20 people, most of them women.
Half-Way Covenant
A Puritan church document: In 1662, allowed partial membership rights to persons not yet converted into the Puritan church.
Rhode Island
Roger Williams along with other colonist such as Anne Hutchinson were the founders of Rhode Island. They were forced into exiled from the Massachusetts bay colony for beliefs about separation of church and freedom of religion.
Middle Colonies
Pennsylvania, New York, Delaware, and New Jersey. They had many religions and different peoples, so it was considered the melting pot of the colonial time.
William Penn
Prominent Quaker granted a colony (Pennsylvania) by Charles II, held it as a personal proprietorship, saw colony as a haven for co-coreligionists. Caused a rise in migration and attempted to treat Native Americans fairly.
Slave Songs
Field workers used songs to pass the time and retained African rhythms, a way to secretly talk to each other, express’s faith and despair through song along with hopes for freedom.
Autonomy
Independent or to have some form of self-government freedom to express one’s own culture and lifestyle without oppression. Many Africans oppressed and could not celebrate their culture.
Syncretism
Unification of opposing people, ideas, or practices, frequently in the realm of religion.
British West Indies
These Caribbean Islands served as bases for the Spanish to invade the Americas.
Town Meetings
A town-wide meeting to decide on issues facing the village and choose a group of people to govern the town for the coming year, restricted to adult male residents.
Massachusetts Legislature (Massachusetts General Court)
Only free, white, male, property owners, who were members of a congregationalist church could vote for these people in the yearly elections.
Transatlantic Trade
A trade route originating in Europe that was used to supply colonies in the New World with slave labor. These raw materials would be taken back to Europe, where they would be used to manufacture goods, thus beginning the cycle of trade again.
Middle Passage
The forced journey that slaves made from Africa to America throughout the 1600's; it consisted of the dangerous trip across the Atlantic Ocean; many slaves perished on this segment of the journey.
Destruction of the Huron
Iroquois attacked Hurons and gave their furs to the Dutch, 1/2 Huron population dies from smallpox, Hurons either died or joined Iroquois.
Beaver Wars
Iroquois attacked Hurons and gave their furs to the Dutch, 1/2 Huron population dies from smallpox, Hurons either died or joined Iroquois.
Chickasaw Wars
Chickasaw fought with the British against French who were allied with the Choctaws and the Illinois Confederation over territory that the French wanted in Mississippi. War came to an end after the French gave up New France in the Treaty of Paris.
King Williams War
Northern conflict fought between the French and the English before France forfeited their colonies in the Treaty of Paris.
Queen Anne’s War
Fought between the French, Spanish, and English colonies for control of the American continent. Each side had various Native allies. The war was fought on four fronts (South, New England. Newfoundland, and Nova Scotia)
Massachusetts Becomes Royal Colony
Massachusetts got in trouble with the English Crown due to voting issues, discrimination against Anglicans, and illegal mint (coins). This leads to Mass. being made a royal colony, and the Crown taking direct ownership of it, angering the locals.
Dominion of New England
Britain consolidated all of their New England colonies into one, angering 3 years of revolts by the colonists.
Navigation Acts
British tell colonists they have to use British sailors, ships, and ports only.
Wool Acts
Limits sale of wool to British territories only.
Molasses Act
British tell the colonists that they must pay taxes if buying molasses from anyone other than British colonies.
King Philip’s War (Metacom’s War)
Conflict between Native Americans in New England and the colonists. Metacom was the Wampanoag chief who began the war after several transgressions by colonists.
Pequot War
Pequot defeat to the colonists of Mass. bay, Plymouth, and Saybrook colonists. 
Yamasee War
Conflict between Settlers of Carolina and the Yamasee. Yamasee and their allies ravaged colonies and forced a colonist retreat, until the Cherokee allied with the Colonists and forced an unstable peace.
Praying Towns
Puritan towns which invited Natives to live with them. Converted Natives to Christianity, and taught colonist ideas. These towns aggravated Natives because they took members of tribes away. Led to King Philip’s War.
Pueblo Revolt
Pueblos revolt against Spanish missions that were threatening their land, trade, and culture.
Spanish Mission System
Peaceful yet firm replacement for Encomiendas after they were removed. Natives were forced to live in places similar to Praying Towns.
Spanish Accommodation
Spaniards accommodated some aspects of Native culture.
Pluralism
Diversity of Thought.
Great Awakening
Period of religious revival brought about by John Edwards and George Whitefield. Decline in Puritanism.
Enlightenment
A shift from traditional values to more progressive new ideals based on the sciences. Emphasized democracy, capitalism, etc.
Anglicization
Influence of British culture in other areas.
Autonomous
Self-governance
Trans-Atlantic Print Culture
The spread of prints from the Old World to the new world that spread the Enlightenment and Anglicization.
Protestant Evangelism
Protestants becoming very active in Evangelization due to the Great Awakening.
Salutary Neglect
Britain’s voluntary policy of giving the colonies some forms of autonomy.
Smuggling
Hiding of illegal or otherwise restricted goods in ships to avoid said restrictions.
Port City Slavery
This type of slavery was more common in the North, helped load and unload ships stationed at ports. 
Chattel Slavery
Slaves have the legal status of property and so can be bought and sold like property.
Interracial Marriage Laws
(Miscegenation Laws), banned marriage between blacks and whites in the North and South. 
Perpetuity
A state or quality of lasting forever
Overt Resistance
Such as talking back, hitting their master or running away - could result in being whipped, sold away from their families and friends, or even killed.
Stono Rebellion
The largest slave revolt in the British colonies. On September 9, 1739, a group of about 20 South Carolina slaves assembled and marched to a firearms store. There, they killed the shopkeepers and armed themselves.
Covert Resistance
More hidden, refusal to follow the rules without vocally or outwardly saying so (ex: purposefully working slowly)
Surrogate Family
When families were separated via slavery, others would look after family members
Voodoo
Vodun is the religion practiced by the African American slaves. It was actively suppressed, and they were tried to be converted to Christianity, but still practiced their religion in secret."""

title2 = []
definition2 = []

splitted = unit2.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title2.append(z)
        print(z)
    elif i%2 == 0:
        definition2.append(z)

for i in title2:
    if i == '':
        title2.remove(i)
for z in definition2:
    if z == '':
        definition2.remove(z)

content2 = dict(zip(title2, definition2))

unit3 = """Autonomy
The ability and state of self-governance.
Fort Duquesne
Fort built by the French in contested lands near Pennsylvania. British sent Washington, which started French and Indian war.
Imperial Efforts
The acts in which Britain tried to raise revenue and consolidate the colonies after the 7 Years’ War, (Stamp Acts, Quartering Acts…etc.)
Revenue
Money made. One of the reasons Britain ended Salutary Neglect.
Consolidate
To combine in order to strengthen. i.e. Britain consolidated their New England colonies to strengthen them.
French and Indian War
A part of the Seven Year war, a conflict stemming from the destruction of Fort Duquesne by Washington where Natives fought alongside French in the Mississippi River Basin to keep their land.
Treaty of Paris (1763)
Treaty that ended the Seven Years War. British victory, French surrender all lands in North America, and the British take over. Extremely costly war, causes Britain to raise taxes.
Albany Plan of Union
Benjamin Franklin’s plan to unite the colonies against Britain, did not go well.
Pontiac’s Rebellion
Attack on the colonies by numerous Native tribes who were fearful that Britain would take their lands, having won the 7 Years War.
Encroachments
Entering land owned by another with malicious intent. Refers to the Spanish threatening the land of Pueblo Natives via Spanish Missions.
Proclamation of 1763
Proclamation that stops colonists from going west of the Appalachians so the Natives aren’t angered.
Stamp Act
Required a stamp to the purchased and applied to all paper products. Stamps cost money, which basically made it a paper tax, which angered colonists.
Townshend Acts
Tax on everyday items sich as lead, paint, paper, and tea. Led to revolts, and eventually the Boston Massacre.
Boston Massacre
The killing of 5 colonists by British soldiers who were hit by thrown rocks.
Tea Act
British tax on tea. Caused Boston Tea Party.
Boston Tea Party
Dumping of millions of dollars worth of tea into the Boston harbor as a protest against the Tea Act. Carried out by the “Sons of Liberty”
Intolerable Acts
Also called the Coercive Acts, did many things: Closed the Boston Harbor, Bannewd town meetings, instituted Martial Law, and took land from Massachusetts to give to Canada. Colonists hate this.
“Taxation without Representation”
Important argument against Britain, which posits that the colonies should not be taxed if they have no representation in Parliament.
Social Contract Theory
Created by Jean-Jacques Rousseau, basically implied that all civilized people agree to a subconscious “contract” to be good.
“Consent of the Governed”
The people of a country have to consent to be governed, otherwise they have the right to over-throw the government. This theory was coined by John Locke
Benjamin Franklin
Revolutionary and Enlightenment thinker. The first to draft a plan to unite the colonies (Albany Plan of Union)
Artisans
Skilled tradesmen or craftsmen such as painters.
Sons of Liberty
A group of college-aged men who were the main dissenters (protestors) against Britain, Did the Boston Tea Party, tar-and-feathering, and burned British official’s houses.
Daughters of Liberty
Female version of Sons of Liberty.
Committees of Correspondence
System of communication between revolutionaries, organized by Samuel Adams.
Mobilization
Preparation for war
Patriot
Colonists who wanted to gain independence from Britain.
Loyalist
Colonists who preferred to stay under Britain’s rule.
Thomas Paine’s Common Sense
A book written about the advantages of independence, targeted towards commonfolk. Incredibly important in convincing the American people to fight for independence.
Continental Army
The army of the independence movement.
Declaration of Independence
A document sent to Britain by America that detailed what Britain did wrong, and how America was going to govern itself. Primarily authored by Thomas Jefferson.
Committee of Five
A group of Five members who drafted and presented the Declaration of Independence. Included John Adams, Thomas Jefferson, Benjamin Franklin, Roger Sherman, and Robert Livingston.
Thomas Jefferson
American diplomat, lawyer, architect, philosopher, and founding father. Most notably remembered for being the primary author of the Declaration of Independence.
John Locke
Enlightenment thinker who posited the theory of “Natural Rights” which were the rights of life, liberty, and property.
Natural Rights
Life, liberty, and property.
Lord Cornwallis
Led British troops against George Washington and the colonists.
Crossing the Delaware (Battle of Trenton)
A surprise attack on British troops at Trenton. Decisive victory for America, raised morals.
Saratoga
Turning point of the war, big loss for Britain, and dashed their hopes of separating New England as a British colony.
Marquis de Lafayette
Frenchmen who gained support for America from France, and who helped train troops.
Netherlands
An ally of the Americans during the American Revolution. They (along with France) contributed a lot to the war effort and played a large part in America’s victory.
Valley Forge
Place where many died of starvation and freezing under Washington’s leadership due to lack of supplies, but proves Washington’s strength as a leader.
Baron Von Steuben
An American officer who served as a Major General in the Continental Army and trained many troops, giving American an edge over the British. Also wrote the Army’s drill and training books.
Yorktown
Final battle of the war, big win for America against general Cornwallis.
Treaty of Paris (1783)
Treaty that ends the Revolutionary War. Promised that Loyalists would not be persecuted, and defined borders. USA gained fishing rights, and also opened up Mississippi River area.
Liberty
Freedom
Primogeniture
The right of the eldest son to inherit property and estates of his father.
Entail
Entail required that property could only be left to direct descendants (usually sons), and not to persons outside of the family.
Republic
A form of government in which the people play an integral role in creating, judging, and executing laws.
Democratic Republic
A form of government in which elected officials control power.
Pennsylvania Act of Gradual Emancipation
Plan to abolish slavery over a gradual course of 20 years.
Abigail Adams
Wife of John Adams, wrote the “Don’t forget the Ladies” letter to her husband.
“Republican Motherhood”
Traditional value system that believed women should stay at home and educate children in the ways of life. 
Reverberated
When an idea or action has many effects. 
State Constitutions
Under the articles of confederation, each state has its own constitution 
Articles of Confederation
The first governing document of America. Suffered from weak central government because colonists were fearful of another monarchy.
Central Government
The federal government, responsible for federal laws.
Shay’s Rebellion
A stubborn rebellion by farmers, illustrated the weak central government of the Articles of Confederation.
Constitutional Convention
A meeting to draft the new document to replace the Articles of Confederation. Lasted 5 months, and required lots of compromises.
Federalism
Federalism is one of the ideologies that emerged during the transition from Articles of Confederation -> Constitution. Federalists believed that State and Federal government should balance each others.
Separation of Powers
The idea that each branch of government should be separate, but should balance the others.
Montesquieu
French enlightenment thinker who came up with the idea of separation of powers.
Prohibition of International Slave Trade
North wanted the slave trade banned, but the South wanted to keep slaves. Neither would ratify the constitution if they didn’t get their way, so they agreed on the 3/5 Compromise.
Checks and Balances
The idea that each of the 3 branches of government should exert some form of control over the others so that one cannot hold all the power.
3/5 Compromise
Determined that each slave would be counted as three-fifths of a person for the purpose of apportioning taxes and representation. 
Great Compromise
Popular term for the measure, which reconciled the New Jersey and Virginia plans at the constitutional convention, giving states proportional representation in the House and equal representation in the Senate.
Limited Government
States that government is restricted in what it may do, and everyone has rights (natural rights) that government cannot take away. 
Federalists
Supported a strong central government, advocated the ratification of the new constitution.
Anti-Federalists
Opposed a strong central government, skeptical about undemocratic tendencies in the Constitution, insisted on Bill of Rights; included Thomas Jefferson and James Monroe.
Ratification
Formal approval, final consent to the effectiveness of a constitution, constitutional amendment, or treaty.
Federalist Papers
A collection of essays written by Alexander Hamilton, John Jay, and James Madison explaining how the new government/constitution would work. Their purpose was to convince the New York state legislature to ratify the constitution, which it did.
The Federalist
Supported a strong central government, advocated the ratification of the new constitution.
Alexander Hamilton
First Secretary of the Treasury. He advocated creation of a national bank, assumption of state debts by the federal government, and a tariff system to pay off the national debt.
James Madison
The author of the Constitution and the Bill of Rights, the father of the Federalist party and the fourth President of the United States. 
Bill of Rights
Consist of the first ten Constitutional Amendments, guarantee certain rights to America citizens in all circumstances, put forth by Anti-Federalists, who feared forms of government intrusion on personal liberties.
Enumerated
Powers of the federal government that are specifically addressed in the Constitution.
Factions
Political groups that agree on objectives and policies, the origins of political parties.
Precedents
A decision or action that establishes a sanctioned rule for determining similar cases in the future.
Political Parties
Groups of people with similar political ideas that are usually against another political party.
Federalist Party
Mostly Wealthy Northeasterners that favored a strong centralized federal government, commerce-based economy, loose construction of constitution, national bank, GB sympathy.
Democratic-Republican Party
Led by Thomas Jefferson, believed people should have political power, favored strong STATE governments, emphasized agriculture, strict interpretation of the Constitution, pro-French, opposed National Bank.
Hamilton’s Financial Plan
Establish a national bank, create a federal mint, and impose excise taxes. The bank was conceived to improve and build the nation's credit, as well as create a common currency.
Whiskey Rebellion
It was a key incident in the development of the First Two Party System in the United States.
Alien and Sedition Act
(Adam’s Cabinet) Four laws passed by the Federalist-controlled Congress as America prepared for war with France. These laws were designed to silence and weaken the Democratic-Republican Party.
Regionalism/Sectionalism
An American Realist movement that was more focused on poor classes and rural settings, they represented the rural poor's struggles and rejection of urban life.
Nationalism
Political ideology that stresses people's membership in a nation-a community defined by a common culture and history as well as by territory.
Gilbert Stuart
Painted portraits of the Presidents, example of an artisan
Pierre Charles L’Enfant
French architect hired by George Washington to design a new city for the capital.
Little Turtle
The chief of the Miamis. In 1790 and 1791 his armies defeated many American armies and killed hundreds of soldiers and handed the United States what remains one of its worst defeats in the history of the frontier.
Battle of Fallen Timbers
An attack made by American General "Mad Anthony Wayne" against invading Indians from the northwest. The defeat of the Indians ended the alliance made with the British and Indians.
Treaty of Greenville
Gave America all of Ohio after General Mad Anthony Wayne battled and defeated the Indians at the Battle of Fallen Timbers.
Frontier Culture
Rebellious, angry, live off the land, Scots-Irish people. 
Scots-Irish
People who fled their home in Scotland in the 1600s to escape poverty and religious oppression.
Paxton Boys
A group of Scots-Irish men living in the Appalachian hills that wanted protection from Indian attacks.  resented the way that the Eastern part of the state dominated political affairs.
Northwest Territory
Encompassing land northwest of the Ohio River, east of the Mississippi River, and south of the Great Lakes.
Northwest Ordinance
The process by which new states could be admitted into the Union from the Northwest Territory.
Ambiguous
Unclear, doubtful.
Spanish Missions in California
The key instrument of Spain's expansion on the frontier. The Spanish wanted to convert Native Americans in the region to Christianity and settle them as farmers on mission lands.
Bonded Labor
Employers give high interest loans to families and to pay them off the family works for low wages to pay off the debt.
Jay’s Treaty
To avoid war with Britain, the treaty included a British promise to evacuate outposts on U.S. soil and pay damages for seized American vessels, in exchange for which Jay bound the United States to repay pre-Revolutionary war debts
Pinckney’s Treaty
Treaty between the U.S. and Spain which gave the U.S. the right to transport goods on the Mississippi river and to store goods in the Spanish port of New Orleans.
French Revolution
A social and political revolution in France that toppled the monarchy; created a dilemma for the United States between helping the crown or the people, chose neutrality in the matter.
Non-Intervention (Neutrality) Policy
The principle that external powers should not intervene in the domestic affairs of sovereign states.
XYZ Affair
A diplomatic incident between French and United States diplomats that resulted in a limited, undeclared war known as the Quasi-War.
Washington’s Farewell Address
When he retired from office. It was not given orally but printed in newspapers. It did not concern foreign affairs; most of it was devoted to domestic problems.
Partisan Debates
Intense political controversy followed the creation of the Constitution regarding topics such as Alexander Hamilton's economic policies"""

title3 = []
definition3 = []

splitted = unit3.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title3.append(z)
        print(z)
    elif (i%2) == 0:
        definition3.append(z)

for i in title3:
    if i == '':
        title3.remove(i)
for z in definition3:
    if z == '':
        definition3.remove(z)

content3 = dict(zip(title3, definition3))

unit4 = """1st Political System
The first system of Government in America. Consisted of two sides: the Federalists (Federalists were in favor of more powerful Federal government) and the Democratic-Republicans (Were in favor of state’s rights)
Tariff
A tariff is a tax imposed by a government on imports or exports of goods.
Virginia/Kentucky Resolutions
Stated that the Alien and Sedition acts were unconstitutional 
Marshall Court
The court run by Justice John Marshall who made 3 famous rulings (Marbury v. Madison, McCulloch v. Madison, and Gibbons v. Ogden), and who was known for 
Marbury v. Madison
Marbury v. Madison, 5 U.S. 137, was a landmark U.S. Supreme Court case that established the principle of judicial review in the United States, meaning that American courts have the power to strike down laws, statutes, and some government actions that they find to violate the Constitution of the United States.
Judicial Review
The ability of US courts to strike down laws, statutes, and some government actions that are found to be unconstitutional.
McCulloch v. Maryland
McCulloch v. Maryland, 17 U.S. 316, was a landmark U.S. Supreme Court decision that defined the scope of the U.S. Congress's legislative power and how it relates to the powers of American state legislatures. The dispute in McCulloch involved the legality of the national bank and a tax that the state of Maryland imposed on it.
Gibbons v. Ogden
Gibbons v. Ogden, 22 U.S. 1, was a landmark decision in which the Supreme Court of the United States held that the power to regulate interstate commerce, granted to Congress by the Commerce Clause of the United States Constitution, encompassed the power to regulate navigation.
2nd Political System
The political system that rose to power after the fall of the Federalists and Democratic-Republicans. The 2nd political system consisted of the Democrats (Led by Andrew Jackson) and the Whigs (Led by Henry Clay). The Democrats were mostly Southerners and wanted less Federal power. The Whigs were mostly Northerners and favored stronger federal government.
Hartford Convention
A convention held by Federalists in 1812, in which they complained about war and threatened to have the North secede rom the union. 
Democrats
Led by Andrew Jackson, wanted less federal power and were mostly Southerners.
Andrew Jackson
Democratic politician and eventual president/war hero. Wins election of 1824 by fighting for the “common man”.
Whigs
Led by Henry Clay, wanted more federal power and were mostly Northerners.
Henry Clay
Whig politician. led the Whig party with experience from work in Britain. Wrote the Missouri Compromise and averted Civil War a couple times.
Infrastructure
Infrastructure is the set of fundamental facilities and systems that support the sustainable functionality of households and firms. Serving a country, city, or other area, including the services and facilities necessary for its economy to function.
Regionalism
Showing preference for your region/section over the whole country
Expanded Suffrage in 1820s
Andrew Jackson expands voting rights as state constitutions are re-written, and the property requirement to vote is removed.
Jacksonian Democracy
Jacksonian Democracy is a term used to describe the expanded power of the Federal Government and expansion of voting rights that occurred under Andrew Jackson. This is the period in which Jackson is most compared to a king (i.e. “King Jackson” political cartoon)
Spoils System
In politics and government, a spoils system is a practice in which a political party, after winning an election, gives government civil service jobs to its supporters, friends, and relatives as a reward for working toward victory, and as an incentive to keep working for the party.
2nd Great Awakening
The 2nd Great Awakening was a rise of Democratic and Individualistic beliefs in the early 1800s. This includes greater social mobility, the rise of rationalism, and the market revolution.
Charles G. Finney
A “Revivalist” preacher that advocated for Protestant teachings and led abolitionist movements, as well as supporting the Underground Railroad.
Revivalists
Followers of a renewed, stricter Protestantism that emerged during the 2nd Great Awakening. Preached strict adherence to biblical teachings and aiming for perfection. 
Rationalism
A philosophical movement that valued reason and knowledge over religious beliefs and emotion.
Utopian Communities
Attempts in the mid-late 1800s to create “perfect” societies. Examples include the Brook Farm, the Fruitlands, New Harmony, and Oneida. Usually created by Transcendentalists.
Shakers
A limb of the Quaker religion. Known for ecstatic behavior during worship. Women and men took equal places in church. Some notable leaders include Jane Wardley, Mother Ann Lee, and Mother Lucy Wright.
Mormons
A religious denomination of the Latter-Day Saints that fled to Illinois to get away from persecution.
National Culture
In America, was a combination of the emerging middle class (An American element); Regional influences such as industrialization, immigration, and frontier living; and European influences such as Liberal and Romantic ideas.
John James Audubon
An American ornithologist, naturalist, and painter. His combined interests in art and ornithology turned into a plan to make a complete pictoral record of all the bird species of North America
Hudson River School
A 19th century American art school which was very focused on Romanticism through landscape paintings.
Transcendentalism
A philosophical movement that believed in the inherent goodness of people and nature, but that society had corrupted the purity, and that people are at their best when independent and self-reliant.
Ralph Waldo Emerson
Transcendentalist leader.
Henry David Thoreau
Transcendentalist leader.
Emerging Middle Class
(At the time) Uniquely American concept that resulted from the breaking of social norms after Enlightenment and Great Awakening(s)
1800s Reforms
Reforms that began as a partial result of the 2nd Great Awakening. All were voluntary and formed outside of gov. Encouraged temperance (Prohibition), public schooling, prisons and mental hospitals, abolitionism, women’s rights.
Abolitionism
Movement to end slavery.
Nat Turner
Led a rebellion in 1832 that lasted several months. Led to 50 deaths. Generally harmed case for abolition, at least in South.
William Lloyd Garrison
White editor of “The Liberator”, an abolitionist magazine that spread abolitionist ideas in the North.
Frederick Douglass
Most well-known abolitionist, well educated slave who escaped to the North and wrote powerful speeches and essays against slavery.
Grimke Sisters
Daughters of South Carolinian slave holder, well known abolitionists as well as suffragettes.
Temperance
Abstaining from alcohol.
Horace Mann
Promoted public education as part of the frontier. Whig.
Dorothea Dix
Woman known for promoting mental health awareness, as well as prison reform. Credited with creating the first mental hospital. 
Women’s Rights Movement
A movement in the early 1800s that advocated for suffrage, and the equal treatment of men and women under the law.
Seneca Falls Convention
A women’s rights conference that produced the “Declaration of Sentiments”
Elizabeth Cady Stanton
One of the organizers of the Seneca Falls Convention.
Declaration of Sentiments
A sort of “declaration of independence” but for women, stating that they believed they should be equal to men.
Cult of Domesticity
Part of Republican Motherhood, encouraged women to remain in the home, being domestic servants of a sort.
Industrial Revolution
A transition to manufacturing-oriented society which began in the early 1800s via the invention of new goods and cheaper labor.
Market Revolution
The market revolution was the expansion of the economic market as a result of improving infrastructure in the early 1800s.
Samuel Slater
Defied a ban from Britain, and shared information about steam power with America.
Eli Whitney
Inventor of the cotton gin
Interchangeable Parts
Idea that goods should be made with components that can be replaced in the event of failure. Popularized by Eli Whitney
Cotton Gin
A device that separated the cotton from the seeds, making cotton very easy to produce and thus very profitable.
Industrial Revolution Inventions
Various machines that made goods cheaper, faster, and easier to produce.
Infrastructure
Government-built utilities such as roads and bridges that served the American people.
National Road
620-mile road from the Potomac and Ohio rivers. Major road.
Erie Canal
Largest construction project of the time, was a 363 mile waterway that linked the Great Lakes to the Atlantic Ocean.
Semi-Subsistence Farming
Farming enough to feed yourself and your family with just a little on the side.
Telegraph
Machine that could send audio signals across long distances, revolutionized communication.
Standard of Living
A concept that describes the general living conditions of a population.
International Migration in Early 1800s
Large number of migrant workers seeking jobs immigrate to the American Northwest and Midwest. 
Ohio River Communities
Communities built on very fertile land, very contested area.
Northern Economy
Mainly focused on industrialization and manufacturing.
Southern Economy
Still reliant on farming, begins to lag behind Northern Economy.
Nationalism
The collective spirit/identity of a nation. More specifically, strict adherence to that identity when faced with change.
American System
Henry Clay’s 3-point Financial Plan that wanted to revitalize the BUS, improve infrastructure, and create new tariffs for revenue and protection from English industries.
Bank of United States (BUS)
A central bank that created (among other things) the common currency we have today.
Louisiana Purchase
A 15 million dollar purchase of land from the French that doubled the size of the USA. 
Lewis and Clark
A pair of explorers who led 46 men to map large parts of the Louisiana Purchase. Hired by Jefferson.
Thomas Jefferson
Third president. Bought lands from the French through the Louisiana Purchase (without congressional approval)
Diplomacy
The art and practice of conducting negotiations between nations.
War of 1812
War between the US and the British/Natives. War ends in a draw and Britain doesn’t bother ‘Merica again.
Impressment
The act or policy of seizing persons and compelling them to serve in the military, especially in naval forces.
Shawnee Indians
The Shawnee are an ethnic group indigenous to North America. In colonial times they were a semi-migratory Native American nation, primarily inhabiting areas of the Ohio Valley.
Monroe Doctrine
Anti-European Imperialist doctrine written by James Monroe. Posited that any European imperialist action in the Americas was a direct threat to USA.
James Monroe
American politician most famously known for the Monroe Doctrine. Also served as the fifth president.
Frontier
Largely immigrant-based, poor communities that survived on the Western frontier of the US.
Seminole Wars
Largely fought in Spanish-owned Florida, these conflicts drove out the Native populations in the area.
Creeks War
The Creeks War was a regional war between opposing Creek factions, European empires and the United States, taking place largely in today's Alabama and along the Gulf Coast. The major conflicts of the war took place between state militia units and the "Red Stick" Creeks.
Indian Removal Act
A law passed by Andrew Jackson that dictated that all Native tribes must forfeit their land and relocate to new reservations in the West.
Worcester v. Georgia
A supreme court case that held that the Georgia criminal statute that prohibited non-Native Americans from being present on Native American lands without a license from the state was unconstitutional. The opinion is most famous for its dicta, which laid out the relationship between tribes and the state and federal governments. It is considered to have built the foundations of the doctrine of tribal sovereignty in the United States.
Trail of Tears
A series of forced Native relocations that killed over 4,000 on its way.
Southern Defenses of Slavery
South argued that Black people were inferior to white people, and due to that, holding them as slaves was the most humane thing to do.
Missouri Compromise
The Missouri Compromise was United States federal legislation that admitted Missouri as a slave state, in exchange for legislation which prohibited slavery north of the 36°30′ parallel except for Missouri.
Nullification Crisis
The Nullification Crisis was an event that almost catalyzed the Civil War. It describes the crisis that faced Andrew Jackson when a tariff is rejected by the states and South Carolina tries to secede."""

title4 = []
definition4 = []

splitted = unit4.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title4.append(z)
        print(z)
    elif i%2 == 0:
        definition4.append(z)

for i, z in zip(title4, definition4):
    if i == '':
        title4.remove(i)
    if z == '':
        definition4.remove(z)

content4 = dict(zip(title4, definition4))

unit5 = """Westward Migration 
Movement of settlers into the American West, began with the Louisiana Purchase and was fueled by the Gold Rush, the Oregon Trail and a belief in "manifest destiny."
California Gold Rush 
Americans migrated west of America in an attempt to get rich off of gold found in Californian rivers 
Comstock Lode 
first major U.S. discovery of silver ore, after the discovery was made public in 1859, prospectors rushed to the area and scrambled to stake their claims.
Homestead Act 
a federal law promoting westward expansion by allotting 160 acres of free public land to individual settlers.
Mormons 
are members of the Church of Jesus Christ of Latter-Day Saints. Founded by Joseph Smith during the Second Great Awakening.
Joseph Smith
founder of Mormonism. Smith wrote the Book of Mormon in 1830. 
“Superiority of American Institutions”
feelings that America’s political and social setup is better than the rest of the worlds 
Manifest Destiny
a philosophy that the United States had a God-given right to “overspread” the continent. At the heart of the doctrine was the notion that Americans were a superior people with superior governmental institutions, and they had superior moral character.
Annexation of Texas
1845-Texas seceded from Mexico and declared independence in response to Mexican abolition of slavery. US adopts/annexes Texas because Southern states support Texas slavery. The North feared expansion of slavery and war with Mexico
James K. Polk
whose four pronged approach to presidency was: reestablish the independent treasury system, reduce tariffs, acquire Oregon, and acquire California and New Mexico from Mexico.
Mexican American War
an armed conflict between the United States and Mexico from 1846 to 1848 in the wake of the 1845 U.S. annexation of Texas, which Mexico considered part of its territory despite the 1836 Texas Revolution.
Treaty of Guadalupe Hidalgo
Ended Mexican American War; Mexico gave up all claims to land from Texas to California for $15 million.
Gadsden Purchase
the 1853 treaty in which the United States bought from Mexico parts of what is now southern Arizona and southern New Mexico.
Wilmot Proviso
a rider (or provision) attached to an appropriations bill during the Mexican War. It stated that slavery would be banned in any territory won from Mexico as a result of the war.
Compromise of 1850
a group of five laws passed in September of 1850. These laws made concessions to both free and slave states to placate both sides of the slavery debate and preserve the union.
Free-Soil Party
A political party with the main purpose of stopping the expansion of slavery in western territories, arguing free men on free soil. The Free-Soil Party was against slavery in the new territories. They also advocated federal aid for internal improvements and urged free government homesteads for settlers.
Pacific Railroad Act
Called for the building of the Transcontinental Railroad to stretch across America connecting California and the rest of America.
Clipper Ships
American boats built during the 1840's in Boston, that were sleek and fast but inefficient in carrying a lot of cargo or passengers.
Commodore Matthew Perry
The Commodore of the U.S. Navy who compelled the opening of Japan to the West with the Treaty of Kanagawa in 1854. Japan also agreed to help shipwrecked soldiers as a result.
U.S. Missionaries in Asia
Sent mostly female missionaries to convert the Asian’s and Americanize them 
Immigration
in Mid-1800s the start of the new immigrants came during the mid 1800’s and they were mistreated. 
Nativism
a person who favors those born in his country and is opposed to immigrants, specifically, a native-born American who wants to limit immigration (and outside influence).
Xenophobia
A general fear or dislike of foreigners; popular among the older generations during the 1880s and 1890s due to the rapid immigration rates.
Know-Nothings (American Party)
A political party who pretended they saw no evil nor did anything regarding said evil. 
Louisville riots
when the anger of working-class New Yorkers over a new federal draft law during the Civil War sparked five days of some of the bloodiest and most destructive rioting in U.S. history.
Baltimore Mayoral Elections
the election of mayors in Baltimore. 
Sitting Bull
leader of the Sioux tribe, he led his people against the United States policies. He was killed by Indian agency police on a reservation, during an attempt to support the Ghost Dance movement.
Battle of Wounded Knee
a massacre in 1890 that started when Sioux left the reservation in protest because of the death of Sitting Bull. The US army killed 150 Sioux at wounded knee; last major incident in the great plains.
Mariano Vallejo
A California military commander, politician, and rancher. Shaped California from Mexico and helped gained their independence.
Northern vs. Southern Economy
North relied on factories and industry while the South relied on farming. 
Harriet Tubman
a conductor who helped slaves escape. She was African American and helped over 300 slaves to freedom and became a very outspoken advocate for women's rights.
Underground Railroad
A network of abolitionists that secretly helped slaves escape to freedom by setting up hiding places and routes to the North.
Arguments against slavery
against the god given rights that all men should be free and the constitutional rights. 
Defenses of slavery
they were property and lesser meaning because they were from another nation. 
Kansas-Nebraska ActF
allowed for popular sovereignty in Kansas and Nebraska.
John Brown
An abolitionist who attempted to lead a slave revolt by capturing Armories in southern territory and giving weapons to slaves, was hung in Harpers Ferry after capturing an Armory.
Raid on Harper’s Ferry
an attempt to start an armed slave revolt by seizing a United States Arsenal at Harpers Ferry in Virginia in 1859.
Dred Scott Decision
Supreme Court decision that stated three things: Blacks were not citizens and therefore could not sue in federal courts; Because a slave is their master's property, they can be taken into any territory and held there in slavery; Congress had no power to ban slavery from the territories. 3rd Party System party system during which the Anti-Mason, American, Liberty, and Free-Soil parties emerged.
Republican Party
Political party founded in northern states in 1854 by anti-slavery activists, modernizers and ex-Whigs, the Republican Party quickly became the principal opposition to the dominant Democratic Party.
Abraham Lincoln
16th president of the United States, he promoted equal rights for African Americans in the famed Lincoln- Douglas debates, he issued the Emancipation Proclamation and set in motion the Civil War, but he was determined to preserve the Union, was assassinated by Booth in 1865.
Election of 1860
The election in which Abraham Lincoln was first elected President due to the schism of the Democrats. Caused a chain reaction of southern states to secede from the Union since they were afraid of Lincoln's policies.
Copperheads
A faction of the democratic party formed after the death of Stephen Douglas. A vocal group of Democrats in the Northern United States who opposed the American Civil War, wanting an immediate peace settlement with the Confederates.
Conscriptions
A form of warfare that mobilizes all a society's resources-economic, political and cultural-in support of the military effort.
Anaconda Plan
3 main goals: To gain control of the Mississippi River which would cut the Confederacy into two parts, to blockade the Southern ports, and to capture the Confederate capital of Richmond.
Jefferson Davis
the President of the Southern Confederate States from 1860 to 1865 after their succession from the Union. During this time, Davis struggled to form a solid government for the states to be governed by.
Ulysses S. Grant
an American general and the eighteenth President of the United States (1869-1877). He achieved international fame as the leading Union general in the American Civil War.
Robert E. Lee
General of the Confederate troops; Prosperous in many battles; Defeated at Antietam when he retreated across the Potomac; Defeated at Gettysburg by General Meade's troops, leading to surrender to General Ulysses.
Stonewall Jackson
a confederate general who was known for his fearlessness in leading rapid marches bold flanking movements and furious assaults.
William T. Sherman
Union army general whose march to sea caused destruction to the south. led march to destroy all supplies and resources, beginning of total warfare. He set out from Chattanooga TN on a campaign of deliberate destruction that went across the state of Georgia into SC and then into NC.
Fort Sumter
South Carolina location where Confederate forces fired the first shots of the Civil War in April of 1861, after Union forces attempted to provision the fort. Significance: South ignited the fighting of the Civil War, provoked North to assemble army.
Antietam
battle in Maryland that ended Lee's first invasion of the North. Known for being the bloodiest day in the war and led to the Emancipation Proclamation.
Vicksburg
as a result of this battle, Vicksburg, Mississippi fell to General Ulysses S. Grant and his army.
Gettysburg
A large battle in the American Civil War, took place in southern Pennsylvania from July 1 to July 3, 1863.
Battle of Atlanta
battle occurred on July 22, 1864, during Sherman's Atlanta Campaign
Sherman’s March to the Sea
Union General William Tecumseh Sherman's destructive March through Georgia. An early instance of "Total war"
Suspension of Habeas Corpus
petition requiring law enforcement officers to present detained individuals before a court to determine the legality of the arrest.
Gettysburg Address
a speech given by Abraham Lincoln after the Battle of Gettysburg, in which he praised the bravery of Union soldiers and renewed his commitment to winning the Civil War; supported the ideals of self-government and human rights.
Lincoln’s 2nd Inaugural Address
Was meant to help heal and restore the country after four years of Civil War.
Emancipation Proclamation
issued by Lincoln to free all the slaves in the Confederate states.
Reconstruction Period
after the Civil War during which Northern political leaders created plans for the governance of the South and a procedure for former Southern states to rejoin the Union.
Civil War Amendments
passed as a result of the outcome of the civil war.
13th Amendment
Constitutional amendment prohibiting all forms of slavery and involuntary servitude. Former Confederate States were required to ratify the amendment prior to gaining reentry into the union.
14th Amendment
All persons born or naturalized in the US are citizens of the US and of the state where they reside.
15th Amendment
quickly passed by Republicans that forbade either the federal government or the states from denying citizens the right to vote based on race, color, or "previous conditions of servitude".
Presidential
Reconstruction A period after the civil war when Lincoln originally. set up the Ten-Percent Plan stating that most Southerners could reinstate. themselves if 10 percent of the voters pledged an oath of allegiance.
Radical Republican
Reconstruction Congressional group that wished to punish the South for its secession from the Union; pushed for measures that gave economic and political rights to newly freed blacks in the South and that made it difficult for former Confederate states to rejoin the Union.
Andrew Johnson
A Southerner form Tennessee, as V.P. when Lincoln was killed, he became president. He opposed radical Republicans who passed Reconstruction Acts over his veto.
Impeachment
to accuse a public official of misconduct in office. The Jeffersonians were angry about a ruling made by Chief Justice John Marshall. The House of Representatives attempted to impeach the unpopular Supreme Court Justice, Samuel Chase.
Freeman’s Bureau
created by Congress in 1865 intended to be like a welfare agency; it was to provide food, clothing, medical care, and education to freedmen and white refugees. Oliver Howard.
Morehouse College
A private, historically black college for men, Morehouse College opened in 1867 to train former slaves to be Protestant ministers and educators.
Sharecropping
a system where the landlord/planter allows a tenant to use the land in exchange for a share of the crop. This encouraged tenants to work to produce the biggest harvest that they could and ensured they would remain tied to the land and unlikely to leave for other opportunities.
Tenant Farming
a system of agriculture whereby farmers cultivate crops or raise livestock on rented lands.
Black Codes
sometimes called Black Laws, were laws governing the conduct of African Americans.
KKK
a viciously racist white supremacist organization that first arose in the South after the end of the Civil War.
Robert Smalls
famous black leader of Civil War-Reconstruction era, hijacked Confederate ship and surrendered it to the Union, later elected to U.S. Congress. minimal Reconstruction.
Hiram Revels
a minister in the African Methodist Episcopal Church, a Republican politician, and college administrator.
Panic of 1873
the first global depression brought about by industrial capitalism. It was caused by too many railroads and factories being formed than existing markets could bear and the over-loaning by banks to those projects.
Death of Charles Sumner
an American statesman and United States Senator from Massachusetts. South Carolina Democratic congressman Preston Brooks nearly killed Sumner with a cane on the Senate floor after Sumner delivered an anti-slavery speech, "The Crime Against Kansas."
White League
a white paramilitary terrorist organization started in the Southern United States in 1874 to intimidate freedmen from voting and politically organizing.
Poll Taxes
a tax levied as a fixed sum on every liable individual. In the United States, voting poll taxes (whose payment was a precondition to voting in an election) have been used to disenfranchise impoverished and minority voters (especially under Reconstruction).
Literacy Tests
in the United States, between the 1850s and 1960s, literacy tests were administered to prospective voters, and this had the effect of disenfranchising African Americans and others.
Compromise of 1877
an informal agreement between southern Democrats and allies of the Republican Rutherford Hayes to settle the result of the 1876 presidential election and marked the end of the Reconstruction era."""

title5 = []
definition5 = []

splitted = unit5.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title5.append(z)
        print(z)
    elif i%2 == 0:
        definition5.append(z)

for i, z in zip(title5, definition5):
    if i == '':
        title5.remove(i)
    if z == '':
        definition5.remove(z)

content5 = dict(zip(title5, definition5))

unit6 = """2nd Industrial Revolution
A second industrial revolution that came with steam power, trains and the like.
Pacific Railways Acts
A series of acts of Congress in 1862 that permitted the construction of a “transcontinental railroad across America.
Transcontinental Railroad
An almost 2,000 mile railroad from Iowa to San Francisco. First of its kind.
Chinese Labor
Immigrants from China come to the US and are exploited for cheap labor.
Taylorism
A work philosophy that dictated the following: “The task of factory management is to determine the most efficient way for the worker to do the job, and to provide incentives for good performance.”
Monopoly
An economic concept which is defined as when all supply of a particular commodity is provided by a single entity.
Trust
A way of consolidating many companies into one larger entity.
Holding Company
Companies that hold large amounts of stock in other companies in order to control them.
Sears Catalogue
A catalogue where people could order any number of consumer goods.
Standard of Living Increase
Americans begin to become wealthier on average as the economy grows and people have expendable income.
Big Business
The growth of monopolies and trusts.
John D. Rockefeller
One of the first people to own a monopoly. Pioneered vertical and horizontal integration.
Standard Oil Company
Rockefeller’s Oil Company
Andrew Carnegie
Basically owned the U.S. Steel market, worth ~72 billion dollars.
Cornelius Vanderbilt
Held a monopoly over the railroads and shipping economies.
JP Morgan
Monopolized banking.
Sanford Dole
Operated pineapple and banana empires. Worked in Hawaii, and was part of the coup that overthrew one of their queens.
Annexation of Hawaii
The US annexes Hawaii after funding a coup d’etat.
Boxer Rebellion
A rebellion of Chinese Boxers who believed that China was becoming too westernized.
Open Door Policy
USA just wants an “open door” for trade with China
“Big Brother” Policy
A US Government policy that dictated America be the “big brother” of Latin America, and thus “encourage trade and cooperation” between the two
James G. Blaine
Originator of the “Big Brother” policy
Spanish-American War
The USS Maine is destroyed via a gas leak, but Spain is blamed. The two go to war, America wins as well as gains the Philippines, Puerto Rico, and Guam. Cuba also freed.
Valeriano Weyler
Spanish ruler of Cuba before the Spanish-American War
Yellow Journalism
Exaggerated press. Played a heavy part in American sympathy for Cuba
De Lome Letter
Spanish letter heavily critical of US president McKinley, intercepted by USA.
USS Maine
A ship that blew up and began the Spanish American War. Blew up because of a gas leak, but was used as a scapegoat to declare war.
Puerto Rico, Guam, Philippines
Territories gained by America after Spanish American war.
Philippine-American War
A rebellion of Philippinos against new American rule, was won by America.
Laissez- Faire Economics
When the government takes a “hands off” approach to its economy.
Xenophobia/Nativism
Fear or hatred of immigrants.
“Old” Immigrants
Northern and Western immigrants who came to America before “New” Immigrants.
“New” Immigrants
New immigrants from Southern and Eastern European Europe.
Child Labor
Use of children as workers
Labor vs. Management
Workers fight against management over poor work conditions and stuff.
Industrial Unrest
Era in which workers unionize and fight for their rights.
Union
Groups formed by workers that advocated for better working conditions, or else they would “strike”
Knights of Labor
One of the biggest unions, and one of the first
American Federation of Labor (AFL)
Another union
Samuel Gompers
Founder of the AFL.
Pullman Strike
A large railroad strike that left 50 dead and 40 million dollars in losses.
New South
Movement to industrialize the south in the late 1800s. 
Henry Grady
Leader of the “New South” movement, great orator.
Grain Elevator
Used to store grain and allow railroad transportation of grain easily. Were large towers that trains would back under to fill up in.
The Grange
Farming protest group created to push back against big business.
Farmers’ Alliance
A whites only pro-farmer organization, similar to the Grange. Replaced Grange over time.
Colored Farmers’ Alliance
Farmer’s Alliance but for minorities.
People’s (Populist) Party
A political party popular in the late 1800s in response to big business. Was short lived, but very influential. Advocated for stronger government control of economic system.
Grange Laws
The Grange Laws, passed in 1880s, were a set of laws that created railroad commissions to supervise railroad rates and policies, as well as the Interstate Commerce Commission, and new Insurance and utility regulatory companies.
Boll Weevil
A bug that destroyed cotton buds and devastated the southern industry.
Demise of Populist Party
The populist party failed because it never gained a foothold in the North, and was portrayed as being “too favorable” for African Americans.
Urbanization
The process of a city and its surrounding areas becoming more populated with middle class people.
Ellis Island
Main immigration point for new immigrants.
Jews Flee Russia
Jewish people fled Russia to escape religious persecution
Horatio Alger
Original “rags to riches” story.
Little Italy
Concentrated group of Italian immigrants who made a cultural haven for themselves.
Chinatowns
Little Italys but for Chinese people.
Assimilation
When a minority group adapts to the customs of a majority group.
Americanization
When immigrants are taught/ expected to be more “American”
American Protective Association
Anti immigration group from the late 1800s.
Chinese Exclusion Act of 1882
Banned Chinese immigrants due to anti-Chinese sentiment.
Political Machines (Boss Politics)
When an individual dominates city or state (local) politics. Most were corrupt, organized, and concerned only with maintaining their power.
Boss Politics and Immigrant Relationship
Bosses exploited working class immigrants, and targeted them.
Boss Tweed/Tammany Hall
One of the most famous Political Machines, operated out of New York
Soapy Smith/Huey Long
A Denver Boss
Expanding Middle Class
Increased access to higher education means more leisure time and expanded consumer culture. Builds a middle class.
New Leisure Activities
New activities that Americans can do because of expendable income.
Vaudeville Shows
Vaudeville is a theatrical genre of variety entertainment born in France at the end of the 19th century. A vaudeville was originally a comedy without psychological or moral intentions, based on a comical situation
New Consumer Culture
As Americans made more money and had more leisure time, a culture of consumerism emerged, supplying pastimes and goods for the new middle class.
Fredrick Turner’s Frontier Thesis
The idea that the frontier was once an opportunity for human independence, and that the frontier was closing.
“Safety-Valve” Theory
Frederick Turner’s theory that the frontier was a safe place of sorts for failing Americans to go and rebuild, and now that it was closed things would only get worse.
Boomtowns
Cities that exploded in population when gold/silver were found.
Indian Wars
A series of battles and wars that resulted in the US government taking Native lands from native tribes.
Destruction of the Buffalo
The Americans killed and drove away a lot of buffalo from Native territory.
Sand Creek Massacre
The Sand Creek massacre was a massacre of Cheyenne and Arapaho people by the U.S. Army in the American Indian Wars that occurred on November 29, 1864, when a 675-man force of the Third Colorado Cavalry under the command of U.S. Volunteers Colonel John Chivington attacked and destroyed a village of Cheyenne and Arapaho people in southeastern Colorado Territory, killing and mutilating an estimated 70–500 Native Americans, about two-thirds of whom were women and children.
Little Big Horn
The Battle of the Little Bighorn, known to the Lakota and other Plains Indians as the Battle of the Greasy Grass and also commonly referred to as Custer's Last Stand, was an armed engagement between combined forces of the Lakota, Northern Cheyenne, and Arapaho tribes and the 7th Cavalry Regiment of the United States Army.
Ghost Dance Movement
Indian ritual to bring back Bison that had been driven off their lands. Scared Americans and was a major catalyst in the Indian Wars.
Dawes Act
A law passed in 1887 that created a land allotment system for Native American tribes, and forcefully took Native lands with the exception of some reservations.
Indian Assimilation
Americans tried to assimilate Native children, failed.
Failure of Reservations to Assimilate
Natives did not accept the concept of rule by force.
Sitting Bull
Sitting Bull was a Hunkpapa Lakota leader who led his people during years of resistance against United States government policies. He was killed by Indian agency police on the Standing Rock Indian Reservation during an attempt to arrest him, at a time when authorities feared that he would join the Ghost Dance movement.
Wounded Knee
The Wounded Knee Massacre, also known as the Battle of Wounded Knee, was a domestic massacre of nearly three hundred Lakota people by soldiers of the United States Army. It occurred on December 29, 1890, near Wounded Knee Creek on the Lakota Pine Ridge Indian Reservation in the U.S. state of South Dakota, following a botched attempt to disarm the Lakota camp.
Gilded Age
1870-1900, name reflects the shining exterior look of America that hides the rotten core.
Social Darwinism
The idea that the weak will fall and the strong will rise.
Gospel of Wealth
Carnegie’s idea that having exorbitant amounts of wealth is okay as long as you give most of it away.
Utopians
People who abandon society to start more “perfect” communities.
Socialists
In their purest form, believed all money should be given to the government, and the government will redistribute it in an egalitarian manner.
Settlement House Movement
Movement by Jane Addams that built spaces for immigrants to come and receive help getting established in America.
Jane Addams
Leader of the SHA.
Hull House
Jane Addam’s settlement house.
Plessy v. Ferguson
“Separate but Equal” supreme court decision."""

title6 = []
definition6 = []

splitted = unit6.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title6.append(z)
        print(z)
    elif i%2 == 0:
        definition6.append(z)

for i, z in zip(title6, definition6):
    if i == '':
        title6.remove(i)
    if z == '':
        definition6.remove(z)

content6 = dict(zip(title6, definition6))

unit7 = """Henry Ford 
Henry Ford (July 30, 1863 – April 7, 1947) was an American industrialist and business magnate, founder of the Ford Motor Company, and chief developer of the assembly line technique of mass production. By creating the first automobile that middle-class Americans could afford, he converted the automobile from an expensive curiosity into an accessible conveyance that profoundly impacted the landscape of the 20th century.His introduction of the Model T automobile revolutionized transportation and American industry. 
Model T 
The Ford Model T (colloquially known as the "tin Lizzie", "leaping Lena", "jitney" or "flivver") is an automobile produced by Ford Motor Company from October 1, 1908, to May 26, 1927. It is generally regarded as the first affordable automobile, which made car travel available to middle-class Americans. The relatively low price was partly the result of Ford's efficient fabrication, including assembly line production instead of individual handcrafting. The Ford Model T was named the most influential car of the 20th century in the 1999 Car of the Century competition, ahead of the BMC Mini, Citroën DS, and Volkswagen Beetle. 
New Woman 
The New Woman was a feminist ideal that emerged in the late 19th century and had a profound influence on feminism well into the 20th century. In 1894, Irish writer Sarah Grand (1854-1943) used the term "new woman" in an influential article, to refer to independent women seeking radical change, and in response the English writer 'Ouida' (Maria Louisa Rame) used the term as the title of a follow-up article. The term was further popularized by British-American writer Henry James, who used it to describe the growth in the number of feminist, educated, independent career women in Europe and the United States. 
Flapper 
Flappers were a generation of young Western women in the 1920s who wore short skirts (just at the knee was short for that time period), bobbed their hair, listened to jazz, and flaunted their disdain for what was then considered acceptable behavior. Flappers were seen as brash for wearing excessive makeup, drinking alcohol, smoking cigarettes in public, driving automobiles, treating sex in a casual manner, and otherwise flouting social and sexual norms. As automobiles became available, flappers gained freedom of movement and privacy. 
Stock Market Crash of 1929 
The Wall Street Crash of 1929, also known as the Great Crash, was a major American stock market crash that occurred in the fall of 1929. It started in September and ended late in October, when share prices on the New York Stock Exchange collapsed. It was the most devastating stock market crash in the history of the United States, when taking into consideration the full extent and duration of its aftereffects. 
Black Tuesday 
The Wall Street Crash of 1929, also known as the Great Crash, was a major American stock market crash that occurred in the fall of 1929. It started in September and ended late in October, when share prices on the New York Stock Exchange collapsed. It was the most devastating stock market crash in the history of the United States, when taking into consideration the full extent and duration of its aftereffects. 
Overproduction 
In economics, overproduction, oversupply, excess of supply or glut refers to excess of supply over demand of products being offered to the market. This leads to lower prices and/or unsold goods along with the possibility of unemployment. The demand side equivalent is underconsumption; some consider supply and demand two sides to the same coin – excess supply is only relative to a given demand, and insufficient demand is only relative to a given supply – and thus consider overproduction and underconsumption equivalent. Overproduction is often attributed as due to previous overinvestment – creation of excess productive capacity, which must then either lie idle (or under capacity), which is unprofitable, or produce an excess supply. 
Underconsumption 
Underconsumption is a theory in economics that recessions and stagnation arise from an inadequate consumer demand, relative to the amount produced. In other words, there is a problem of overproduction and overinvestment during a demand crisis. The theory formed the basis for the development of Keynesian economics and the theory of aggregate demand after the 1930s. 
Speculation 
Speculation is the purchase of an asset (a commodity, goods, or real estate) with the hope that it will become more valuable in the near future.  In finance, speculation is also the practice of engaging in risky financial transactions in an attempt to profit from short term fluctuations in the market value of a tradable financial instrument—rather than attempting to profit from the underlying financial attributes embodied in the instrument such as value addition, return on investment, or dividends. Many speculators pay little attention to the fundamental value of a security and instead focus purely on price movements. 
Bull Market 
A market trend is a perceived tendency of financial markets to move in a particular direction over time. These trends are classified as secular for long time frames, primary for medium time frames, and secondary for short time frames. Traders attempt to identify market trends using technical analysis, a framework which characterizes market trends as predictable price tendencies within the market when price reaches support and resistance levels, varying over time. 
Arbitrage 
In economics and finance, arbitrage (, UK also ) is the practice of taking advantage of a price difference between two or more markets: striking a combination of matching deals that capitalize upon the imbalance, the profit being the difference between the market prices at which the unit is traded. When used by academics, an arbitrage is a transaction that involves no negative cash flow at any probabilistic or temporal state and a positive cash flow in at least one state; in simple terms, it is the possibility of a risk-free profit after transaction costs. For example, an arbitrage opportunity is present when there is the possibility to instantaneously buy something for a low price and sell it for a higher price. 
Great Depression 
The Great Depression was a severe worldwide economic depression that took place mostly during the 1930s, beginning in the United States. The timing of the Great Depression varied across the world; in most countries, it started in 1929 and lasted until the late 1930s. It was the longest, deepest, and most widespread depression of the 20th century. 
President Herbert Hoover 
Herbert Clark Hoover (August 10, 1874 – October 20, 1964) was an American politician, businessman, and engineer, who served as the 31st president of the United States from 1929 to 1933. A member of the Republican Party, he held office during the onset of the Great Depression. Before serving as president, Hoover led the Commission for Relief in Belgium, served as the director of the U.S. Food Administration, and served as the third U.S. Secretary of Commerce. 
Hoovervilles 
A "Hooverville" was a shanty town built during the Great Depression by the homeless in the United States. They were named after Herbert Hoover, who was President of the United States during the onset of the Depression and was widely blamed for it. The term was coined by Charles Michelson, publicity chief of the Democratic National Committee. 
Gilded Age 
In United States history, the Gilded Age was an era that occurred during the late 19th century, from the 1870s to about 1900. The Gilded Age was an era of rapid economic growth, especially in the Northern and Western United States. As American wages grew much higher than those in Europe, especially for skilled workers, the period saw an influx of millions of European immigrants. 
Progressive Era 
The  Progressive Era (1896–1916) was  a period of widespread social activism and political reform across the United States of America that spanned the 1890s to the 1920s. Progressive reformers were typically middle-class society women or Christian ministers. The main objectives of the Progressive movement were addressing problems caused by industrialization, urbanization, immigration, and political corruption. 
Muckrakers 
The muckrakers were reform-minded journalists in the Progressive Era in the United States (1890s–1920s) who exposed established institutions and leaders as corrupt. They typically had large audiences in popular magazines. The modern term generally references investigative journalism or watchdog journalism; investigative journalists in the US are often informally called "muckrakers". 
Upton Sinclair 
Upton Beall Sinclair Jr. (September 20, 1878 – November 25, 1968) was an American writer, political activist and the 1934 Democratic Party nominee for Governor of California who wrote nearly 100 books and other works in several genres. Sinclair's work was well known and popular in the first half of the 20th century, and he won the Pulitzer Prize for Fiction in 1943. 
The Jungle 
The Jungle is a 1906 novel by the American journalist and novelist Upton Sinclair (1878–1968). The novel portrays the harsh conditions and exploited lives of immigrants in the United States in Chicago and similar industrialized cities. Sinclair's primary purpose in describing the meat industry and its working conditions was to advance socialism in the United States. 
Lincoln Steffens 
Lincoln Austin Steffens (April 6, 1866 – August 9, 1936) was an American investigative journalist and one of the leading muckrakers of the Progressive Era in the early 20th century. He launched a series of articles in McClure's, called "Tweed Days in St. Louis", that would later be published together in a book titled The Shame of the Cities. 
Ida Tarbell 
Ida Minerva Tarbell (November 5, 1857 – January 6, 1944) was an American writer, investigative journalist, biographer and lecturer. She was one of the leading muckrakers of the Progressive Era of the late 19th and early 20th centuries and pioneered investigative journalism. Born in Pennsylvania at the onset of the oil boom, Tarbell is best known for her 1904 book The History of the Standard Oil Company. 
History of Standard Oil 
The History of the Standard Oil Company is a 1904 book by journalist Ida Tarbell. It is an exposé about the Standard Oil Company, run at the time by oil tycoon John D. Rockefeller, the richest figure in American history. Originally serialized in nineteen parts in McClure's magazine, the book is a seminal example of muckraking, and inspired many other journalists to write about trusts, large businesses that (in the absence of strong antitrust laws in the 19th century) attempted to gain monopolies in various industries. 
Interstate Commerce Act of 1887 
The Interstate Commerce Act of 1887 is a United States federal law that was designed to regulate the railroad industry, particularly its monopolistic practices. The Act required that railroad rates be "reasonable and just," but did not empower the government to fix specific rates.  It also required that railroads publicize shipping rates and prohibited short haul or long haul fare discrimination, a form of price discrimination against smaller markets, particularly farmers in Western or Southern Territory compared to the Official Eastern states. 
Seventeenth Amendment to the United States Constitution 
The Seventeenth Amendment (Amendment XVII) to the United States Constitution established the direct election of United States senators in each state. The amendment supersedes Article I, §3, Clauses 1 and 2 of the Constitution, under which senators were elected by state legislatures. It also alters the procedure for filling vacancies in the Senate, allowing for state legislatures to permit their governors to make temporary appointments until a special election can be held. 
Initiative 
In political science, an initiative (also known as a popular or citizens' initiative) is a means by which a petition signed by a certain minimum number of registered voters can force a government to choose to either enact a law or hold a public vote in parliament in what is called indirect initiative, or under direct initiative, the proposition is immediately put to a plebiscite or referendum, in what is called a Popular initiated Referendum or citizen-initiated referendum. In an indirect initiative, a measure is first referred to the legislature, and then put to a popular vote only if not enacted by the legislature. If the initiative (citizen-proposed law) is rejected by the parliament, the government may be forced to see the proposition put to a referendum. 
Referendum 
A referendum (plural: referendums or less commonly referenda) is a direct and universal vote in which an entire electorate is invited to vote on a particular proposal and can have nationwide or local forms. This may result in the adoption of a new policy or specific law. In some countries, it is synonymous with a plebiscite or a vote on a ballot question. 
Product recall 
A product recall is a request from a manufacturer to return a product after the discovery of safety issues or product defects that might endanger the consumer or put the maker/seller at risk of legal action. The recall is an effort to limit ruination of the corporate image and limit liability for corporate negligence, which can cause significant legal costs. It can be difficult, if not impossible, to determine how costly can be releasing to the consumer a product that could endanger someone's life and the economic loss resulting from unwanted publicity. 
Eighteenth Amendment to the United States Constitution 
The Eighteenth Amendment (Amendment XVIII) of the United States Constitution established the prohibition of alcohol in the United States. The amendment was proposed by Congress on December 18, 1917, and was ratified by the requisite number of states on January 16, 1919. The Eighteenth Amendment was repealed by the Twenty-first Amendment on December 5, 1933. 
Nineteenth Amendment to the United States Constitution 
The Nineteenth Amendment (Amendment XIX) to the United States Constitution prohibits the states and the federal government from denying the right to vote to citizens of the United States on the basis of sex. Initially introduced to Congress in 1878, several attempts to pass a women's suffrage amendment failed until passing the House of Representatives on May 21, 1919, followed by the Senate on June 4, 1919. It was then submitted to the states for ratification. 
Twenty-first Amendment to the United States Constitution 
The temperance movement was a strong force in U.S. politics in the early 20th century, enabling it to win passage of the Eighteenth Amendment. Its influence began to wane, however, in the wake of lax enforcement of prohibition and the emerging illegal economies that quenched the thirst of many American adults. On Feb. 
Conservation Movement 
The conservation movement, also known as nature conservation, is a political, environmental, and social movement that seeks to manage and protect natural resources, including animal, fungus and plant species as well as their habitat for the future. Evidence-based conservation seeks to use high quality scientific evidence to make conservation efforts more effective. The early conservation movement included fisheries and wildlife management, water, soil conservation, and sustainable forestry. 
Preservationism 
Historic preservation (US), heritage preservation or heritage conservation (UK), is an endeavor that seeks to preserve, conserve and protect buildings, objects, landscapes or other artifacts of historical significance. It is a philosophical concept that became popular in the twentieth century, which maintains that cities as products of centuries’ development should be obligated to protect their patrimonial legacy. The term refers specifically to the preservation of the built environment, and not to preservation of, for example, primeval forests or wilderness. 
Theodore Roosevelt 
Theodore  Roosevelt Jr. ( ROH-zə-velt; October 27, 1858 – January 6, 1919), often referred to as Teddy Roosevelt or his initials T. R., was an American statesman, conservationist, naturalist, historian, and writer, who served as the 26th president of the United States from 1901 to 1909. He previously served as 33rd governor of New York from 1899 to 1900 and the 25th vice president of the United States from March to September 1901. 
John Muir 
John Muir ( MEWR; April 21, 1838 – December 24, 1914) also known as "John of the Mountains" and "Father of the National Parks", was an influential Scottish-American naturalist, author, environmental philosopher, botanist, zoologist, glaciologist, and early advocate for the preservation of wilderness in the United States of America. His letters, essays, and books describing his adventures in nature, especially in the Sierra Nevada, have been read by millions. His activism helped to preserve the Yosemite Valley and Sequoia National Park, and his example has served as an inspiration for the preservation of many other wilderness areas. 
Dust Bowl 
The Dust Bowl was a period of severe dust storms that greatly damaged the ecology and agriculture of the American and Canadian prairies during the 1930s; severe drought and a failure to apply dryland farming methods to prevent  the aeolian processes (wind erosion) caused the phenomenon. The drought came in three waves, 1934, 1936, and 1939–1940, but some regions of the High Plains experienced drought conditions for as many as eight years. With insufficient understanding of the ecology of the plains, farmers had conducted extensive deep plowing of the virgin topsoil of the Great Plains during the previous decade; this had displaced the native, deep-rooted grasses that normally trapped soil and moisture even during periods of drought and high winds.  The rapid mechanization of farm equipment, especially small gasoline tractors, and widespread use of the combine harvester contributed to farmers' decisions to convert arid grassland (much of which received no more than 10 inches (~250 mm) of precipitation per year) to cultivated cropland. 
Okie 
"Okie", in the most general sense, refers to a resident, native, or cultural descendant of Oklahoma, equating to  Oklahoman. It is derived from the name of the state, similar to Arkie for a native of Arkansas.  However, the term is most often used more specifically in a pejorative sense. 
New Deal 
The New Deal was a series of programs, public work projects, financial reforms, and regulations enacted by President Franklin D. Roosevelt in the United States between 1933 and 1939.  Major federal programs and agencies included the Civilian Conservation Corps (CCC), the Civil Works Administration (CWA), the Farm Security Administration (FSA), the National Industrial Recovery Act of 1933 (NIRA) and the Social Security Administration (SSA). They provided support for farmers, the unemployed, youth and the elderly. 
Franklin Delano Roosevelt 
Franklin Delano Roosevelt (,  ROH-zə-velt; January 30, 1882 – April 12, 1945), often referred to by his initials FDR, was an American politician who served as the 32nd president of the United States from 1933 until his death in 1945. A member of the Democratic Party, he won a record four presidential elections and became a central figure in world events during the first half of the 20th century. Roosevelt directed the federal government during most of the Great Depression, implementing his New Deal domestic agenda in response to the worst economic crisis in U.S. history. 
Eleanor Roosevelt 
Anna Eleanor Roosevelt (; October 11, 1884 – November 7, 1962) was an American political figure, diplomat and activist. She served as the First Lady of the United States from March 4, 1933, to April 12, 1945, during her husband President Franklin D. Roosevelt's four terms in office, making her the longest-serving First Lady of the United States. Roosevelt served as United States Delegate to the United Nations General Assembly from 1945 to 1952. 
New Deal 
The New Deal was a series of programs, public work projects, financial reforms, and regulations enacted by President Franklin D. Roosevelt in the United States between 1933 and 1939.  Major federal programs and agencies included the Civilian Conservation Corps (CCC), the Civil Works Administration (CWA), the Farm Security Administration (FSA), the National Industrial Recovery Act of 1933 (NIRA) and the Social Security Administration (SSA). They provided support for farmers, the unemployed, youth and the elderly. 
Tennessee Valley Authority 
The Tennessee Valley Authority (TVA) is a federally owned corporation in the United States created by congressional charter on May 18, 1933, to provide navigation, flood control, electricity generation, fertilizer manufacturing, and economic development to the Tennessee Valley, a region particularly affected by the Great Depression. Senator George W. Norris (R-Nebraska) was a strong sponsor of this project. TVA was envisioned not only as a provider, but also as a regional economic development agency that would use federal experts and rural electrification to help modernize the rural region's economy and society. TVA's service area covers most of Tennessee, portions of Alabama, Mississippi, and Kentucky, and small slices of Georgia, North Carolina, and Virginia. 
Federal Deposit Insurance Corporation 
The Federal Deposit Insurance Corporation (FDIC) is one of two agencies that provide  deposit insurance to depositors in U.S. depository institutions, the other being the National Credit Union Administration, which regulates and insures credit unions. The FDIC is a United States government corporation providing deposit insurance to depositors in U.S. commercial banks and savings banks. The FDIC was created by the 1933 Banking Act, enacted during the Great Depression to restore trust in the American banking system. 
Social Security Act 
The Social Security Act of 1935 is a law enacted by the 74th United States Congress and signed into law by US President Franklin D. Roosevelt. The law created the Social Security program as well as insurance against unemployment. The law was part of Roosevelt's New Deal domestic program. 
Wagner Act 
The National Labor Relations Act of 1935 (also known as the Wagner Act) is a foundational statute of United States labor law that guarantees the right of private sector employees to organize into trade unions, engage in collective bargaining, and take collective action such as strikes. Central to the act was a ban on company unions. The act was written by Senator Robert F. Wagner, passed by the 74th United States Congress, and signed into law by President Franklin D. Roosevelt. 
Huey Long 
Huey Pierce Long Jr. (August 30, 1893 – September 10, 1935), byname "The Kingfish", was an American politician who served as the 40th governor of Louisiana from 1928 to 1932 and as a member of the United States Senate from 1932 until his assassination in 1935. He was a populist member of the Democratic Party and rose to national prominence during the Great Depression for his vocal criticism from the left of President Franklin D. Roosevelt and his New Deal. 
Court Packing Bill 
The Judicial Procedures Reform Bill of 1937, frequently called the "court-packing plan", was a legislative initiative proposed by U.S. President Franklin D. Roosevelt to add more justices to the U.S. Supreme Court in order to obtain favorable rulings regarding New Deal legislation that the Court had ruled unconstitutional. The central provision of the bill would have granted the president power to appoint an additional justice to the U.S. Supreme Court, up to a maximum of six, for every member of the court over the age of 70 years and 6 months. In the Judiciary Act of 1869, Congress had established that the Supreme Court would consist of the chief justice and eight associate justices. 
Radio 
Radio is the technology of signaling and communicating using radio waves. Radio waves are electromagnetic waves of frequency between 30 hertz (Hz) and 300 gigahertz (GHz). They are generated by an electronic device called a transmitter connected to an antenna which radiates the waves, and received by a radio receiver connected to another antenna. 
Harlem Renaissance 
The  Harlem Renaissance was an intellectual and cultural revival of African American music, dance, art, fashion, literature, theater and politics centered in Harlem, Manhattan, New York City, spanning the 1920s and 1930s. At the time, it was known as the "New Negro Movement", named after The New Negro, a 1925 anthology edited by Alain Locke. The movement also included the new African-American cultural expressions across the urban areas in the Northeast and Midwest United States affected by a renewed militancy in the general struggle for civil rights for African-Americans that occurred in the wake of civil rights struggles in the then-still-segregated US Armed Forces in WWI and which was further inspired by the NAACP, the Garveyite movement and the Russian Revolution, combined with the Great Migration of African-American workers fleeing the racist conditions of the Jim Crow Deep South, Harlem being the final destination of the largest number of those who migrated north. 
Langston Hughes 
James Mercer Langston Hughes (February 1, 1901 – May 22, 1967) was an American poet, social activist, novelist, playwright, and columnist from Joplin, Missouri. One of the earliest innovators of the then-new literary art form called jazz poetry, Hughes is best known as a leader of the Harlem Renaissance. He famously wrote about the period that "the Negro was in vogue", which was later paraphrased as "when Harlem was in vogue. "Growing up in a series of Midwestern towns, Hughes became a prolific writer at an early age. 
Louis Armstrong 
Louis Daniel Armstrong (August 4, 1901 – July 6, 1971), nicknamed "Satchmo", "Satch", and "Pops", was an American trumpeter, composer, vocalist, and actor who was among the most influential figures in jazz. His career spanned five decades, from the 1920s to the 1960s, and different eras in the history of jazz. Armstrong was born and raised in New Orleans. Coming to prominence in the 1920s as an inventive trumpet and cornet player, Armstrong was a foundational influence in jazz, shifting the focus of the music from collective improvisation to solo performance. 
Red Scare 
A Red Scare is the promotion of a widespread fear of a potential rise of communism or anarchism by a society or state.  The term is most often used to refer to two periods in the history of the United States which are referred to by this name. The First Red Scare, which occurred immediately after World War I, revolved around a perceived threat from the American labor movement, anarchist revolution, and political radicalism. 
Eugene Debs 
Eugene Victor "Gene" Debs (November 5, 1855 – October 20, 1926) was an American socialist, political activist, trade unionist, one of the founding members of the Industrial Workers of the World (IWW) ("Wobblies") and five times the candidate of the Socialist Party of America for President of the United States. Through his presidential candidacies as well as his work with labor movements, Debs eventually became one of the best-known socialists living in the United States. Early in his political career, Debs was a member of the Democratic Party. 
Espionage Act 
The Espionage Act of 1917 is a United States federal law passed on June 15, 1917, shortly after the U.S. entry into World War I. It has been amended numerous times over the years. It was originally found in Title 50 of the U.S. Code (War & National Defense) but is now found under Title 18 (Crime & Criminal Procedure). Specifically, it is 18 U.S.C. ch. 
Alien and Sedition Acts 
The Alien and Sedition Acts were four laws passed by the Federalist-dominated 5th United States Congress and signed into law by President John Adams in 1798. They made it harder for an immigrant to become a citizen (Naturalization Act), allowed the president to imprison and deport non-citizens who were deemed dangerous ("An Act Concerning Aliens", also known as the Alien Friends Act of 1798) or who were from a hostile nation (Alien Enemy Act of 1798), and criminalized making 'false statements' critical of the federal government (Sedition Act of 1798). The Alien Friends Act expired two years after its passage, and the Sedition Act expired on 3 March 1801, while the Naturalization Act and Alien Enemies Act had no expiration clause. 
Fundamentalist Christian 
Christian fundamentalism in its modern form began in the late 19th and early 20th centuries among British and American Protestants as a reaction to theological liberalism and cultural modernism. Fundamentalists argued that 19th-century modernist theologians had misinterpreted or rejected certain doctrines, especially biblical inerrancy, which they considered the fundamentals of the Christian faith. Fundamentalists are almost always described as having a literal interpretation of the Bible. 
Scopes Monkey Trial 
The Scopes Trial, formally known as The State of Tennessee v. John Thomas Scopes and commonly referred to as the Scopes Monkey Trial, was an American legal case in July 1925 in which a high school teacher, John T. Scopes, was accused of violating Tennessee's Butler Act, which had made it unlawful to teach human evolution in any state-funded school. The trial was deliberately staged in order to attract publicity to the small town of Dayton, Tennessee, where it was held. 
Emergency Quota Act of 1921 
The Emergency Quota Act, also known as the Emergency Immigration Act of 1921, the Immigration Restriction Act of 1921, the Per Centum Law, and the Johnson Quota Act (ch. 8, 42 Stat. 5 of May 19, 1921), was formulated mainly in response to the large influx of Southern and Eastern Europeans and successfully restricted their immigration as well as that of other "undesirables" to the United States. 
Bracero Program 
The Bracero program (from the Spanish term bracero, meaning "manual laborer" or "one who works using his arms") was a series of laws and diplomatic agreements, initiated on August 4, 1942, when the United States signed the Mexican Farm Labor Agreement with Mexico. For these farmworkers, the agreement guaranteed decent living conditions (sanitation, adequate shelter and food), and a minimum wage of 30 cents an hour, as well as protections from forced military service, and guaranteed part of wages were to be put into a private savings account in Mexico; it also allowed the importation of contract laborers from Guam as a temporary measure during the early phases of World War II.The agreement was extended with the Migrant Labor Agreement of 1951, enacted as an amendment to the Agricultural Act of 1949 (Public Law 78) by Congress, which set the official parameters for the bracero program until its termination in 1964.A 2018 study published in the American Economic Review found that the Bracero program did not have any adverse impact on the labor market outcomes of American-born farm workers. The end of the Bracero program did not raise wages or employment for American-born farm workers. 
Imperialists 
Imperialism is a policy or ideology of extending the rule over peoples and other countries, for extending political and economic access, power and control, often through employing hard power especially military force, but also soft power. While related to the concepts of colonialism and empire, imperialism is a distinct concept that can apply to other forms of expansion and many forms of government. Expansionism and centralisation have existed throughout recorded history by states, with the earliest examples dating back to the mid-third millennium BC. However, the concept of imperialism arose in the modern age, associated chiefly with the European colonial powers of the 17th, 18th, and 19th centuries and New Imperialism. 
Isolationism 
Isolationism is a category of foreign policies institutionalized by leaders who assert that nations' best interests are best served by keeping the affairs of other countries at a distance. One possible motivation for limiting international involvement is to avoid being drawn into dangerous and otherwise undesirable conflicts. There may also be a perceived benefit from avoiding international trade agreements or other mutual assistance pacts. 
James Blain 
James "Jim" Blain served as the Chief Executive of the Boy Scouts of Canada. In 1990, Blain was awarded the 202nd Bronze Wolf, the only distinction of the World Organization of the Scout Movement, awarded by the World Scout Committee for exceptional services to world Scouting. He was also a recipient of the Silver World Award. 
Pan-American Highway 
The Pan-American Highway (French: (Auto)route panaméricaine/transaméricaine; Portuguese: Rodovia/Auto-estrada Pan-americana; Spanish: Autopista/Carretera/Ruta Panamericana) is a network of roads stretching across the American continents and measuring about 30,000 kilometres (19,000 mi) in total length. Except for a rainforest break of approximately 106 km (70 mi) across the border between southeast Panama and northwest Colombia, called the Darién Gap, the roads link almost all of the Pacific coastal countries of the Americas in a connected highway system. According to Guinness World Records, the Pan-American Highway is the world's longest "motorable road". 
Roosevelt Corollary 
The Roosevelt Corollary was an addition to the Monroe Doctrine articulated by President Theodore Roosevelt in his State of the Union address in 1904 after the Venezuela Crisis of 1902–1903. The corollary states that the United States will intervene in conflicts between the European countries and Latin American countries to enforce legitimate claims of the European powers, rather than having the Europeans press their claims directly. Roosevelt tied his policy to the Monroe Doctrine, and it was also consistent with his foreign policy included in his Big Stick Diplomacy. 
Great White Fleet 
The Great White Fleet was the popular nickname for the group of United States Navy battleships which completed a journey around the globe from December 16, 1907 to February 22, 1909 by order of United States President Theodore Roosevelt.  Its mission was to make friendly courtesy visits to numerous countries while displaying new U.S. naval power to the world. The hulls of these ships were painted a stark white, giving the armada its nickname. It consisted of 16 battleships divided into two squadrons, along with various escorts. 
Panama Canal 
The Panama Canal (Spanish: Canal de Panamá) is an artificial 82 km (51 mi) waterway in Panama that connects the Atlantic Ocean with the Pacific Ocean. The canal cuts across the Isthmus of Panama and is a conduit for maritime trade. One of the largest and most difficult engineering projects ever undertaken, the Panama Canal shortcut greatly reduces the time for ships to travel between the Atlantic and Pacific oceans, enabling them to avoid the lengthy, hazardous Cape Horn route around the southernmost tip of South America via the Drake Passage or Strait of Magellan and the even less popular route through the Arctic Archipelago and the Bering Strait. 
World War I 
World War I (or the First World War, often abbreviated as WWI or WW1) was a global war originating in Europe that lasted from 28 July 1914 to 11 November 1918. Contemporaneously known as the Great War or "the war to end all wars", it led to the mobilisation of more than 70 million military personnel, including 60 million Europeans, making it one of the largest wars in history. It is also one of the deadliest conflicts in history, with an estimated 9 million combatant deaths and 13 million civilian deaths as a direct result of the war, while resulting genocides and the related 1918 Spanish flu pandemic caused another 17–100 million deaths worldwide, including an estimated 2.64 million Spanish flu deaths in Europe and as many as 675,000 Spanish flu deaths in the United States. On 28 June 1914, Gavrilo Princip, a Bosnian Serb Yugoslav nationalist, assassinated the Austro-Hungarian heir Archduke Franz Ferdinand in Sarajevo, leading to the July Crisis. 
Allied Powers of World War I 
The Allies of World War I or Entente Powers were the coalition of countries led by France, Britain, Russia, Italy and Japan against the Central Powers of Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria during the First World War (1914–1918). By the end of the first decade of the 20th century, the major European powers were divided between the Triple Entente and the Triple Alliance. The Triple Entente was made up of France, Britain, and Russia. 
Central Powers 
The Central Powers, also Central Empires, was one of the two main coalitions that fought World War I (1914–18). It consisted of Germany, Austria-Hungary, the Ottoman Empire and Bulgaria; hence it is also known as the Quadruple Alliance. The Central Powers faced and was defeated by the Allied Powers that had formed around the Triple Entente. The Powers' origin was the alliance of Germany and Austria-Hungary in 1879. 
Unrestricted Submarine Warfare 
Unrestricted submarine warfare is a type of naval warfare in which submarines sink vessels such as freighters and tankers without warning, as opposed to attacks per prize rules (also known as "cruiser rules"). Prize rules call for submarines to surface and search merchantmen and place crews in "a place of safety" (for which lifeboats did not qualify, except under particular circumstances) before sinking them, unless the ship showed "persistent refusal to stop ... or active resistance to visit or search". 
Zimmerman Note 
The Zimmermann Telegram (or Zimmermann Note or Zimmerman Cable) was a secret diplomatic communication issued from the German Foreign Office in January 1917 that proposed a military alliance between Germany and Mexico. If the United States entered World War I against Germany, Mexico would recover Texas, Arizona, and New Mexico. The telegram was intercepted and decoded by British intelligence. 
American Expeditionary Force 
The American Expeditionary Forces (A.E.F. or AEF) was a formation of the United States Army on the Western Front of World War I. The AEF was established on July 5, 1917, in France under the command of Gen. John J. Pershing. It fought alongside French Army, British Army, Canadian Army, and Australian Army units against the Imperial German Army. 
League of Nations 
The League of Nations, abbreviated as LON (French: Société des Nations [sɔsjete de nɑsjɔ̃], abbreviated as SDN or SdN), was the first worldwide intergovernmental organisation whose principal mission was to maintain world peace. Founded on 10 January 1920 following the Paris Peace Conference that ended the First World War, it ceased operations on 20 April 1946. The organisation's primary goals, as stated in its Covenant, included preventing wars through collective security and disarmament and settling international disputes through negotiation and arbitration. 
Unilateralism 
Unilateralism is any doctrine or agenda that supports one-sided action. Such action may be in disregard for other parties, or as an expression of a commitment toward a direction which other parties may find disagreeable. As a word, unilateralism is attested from 1926, specifically relating to unilateral disarmament. 
Stimson Doctrine 
The Stimson Doctrine is the policy of nonrecognition of states created as a result of aggression. The policy was implemented by the United States federal government, enunciated in a note of January 7, 1932, to  the Empire of Japan and the Republic of China, of non-recognition of international territorial changes that were executed by force. The doctrine was an application of the principle of ex injuria jus non oritur. 
Washington Naval Conference 
The Washington Naval Conference was a disarmament conference called by the United States and held in Washington, DC from November 12, 1921 to February 6, 1922. It was conducted outside the auspices of the League of Nations. It was attended by nine nations (the United States, Japan, China, France, Britain, Italy, Belgium, Netherlands, and Portugal) regarding interests in the Pacific Ocean and East Asia. 
Neutrality Act of 1939 
The Neutrality Acts were a series of acts passed by the United States Congress in the 1930s (specifically 1935, 1936, 1937, and 1939) in response to the growing threats and wars that led to World War II. They were spurred by the growth in isolationism and non-interventionism in the US following its disillusionment after World War I, and sought to ensure that the US would not become entangled again in foreign conflicts. The legacy of the Neutrality Acts is widely regarded as having been generally negative; they made no distinction between aggressor and victim, treating both equally as belligerents, and they limited the US government's ability to aid Britain and France against Nazi Germany.  The acts were largely repealed in 1941, in the face of German submarine attacks on U.S. vessels and the Japanese attack on Pearl Harbor. 
Lend-Lease Act 
The Lend-Lease policy, formally titled An Act to Promote the Defense of the United States (Pub.L. 77–11, H.R. 1776, 55 Stat. 31, enacted March 11, 1941), was a program under which the United States supplied the United Kingdom (and British Commonwealth), Free France, the Republic of China, and later the Soviet Union and other Allied nations with food, oil, and materiel between 1941 and August 1945. This included warships and warplanes, along with other weaponry. 
Fascist 
Fascism () is a form of far-right, authoritarian ultranationalism characterized by dictatorial power, forcible suppression of opposition and strong regimentation of society and of the economy which came to prominence in early 20th-century Europe. The first fascist movements emerged in Italy during World War I, before spreading to other European countries. Opposed to liberalism, democracy, Marxism, and anarchism, fascism is placed on the far right within the traditional left–right spectrum. Fascists saw World War I as a revolution that brought massive changes to the nature of war, society, the state, and technology. 
Allied Powers of World War II 
The Allies of World War II were the countries that together opposed the Axis powers during the Second World War (1939–1945). The Allies promoted the alliance as a means to defeat German, Japanese and Italian aggression. At the start of the war on 1 September 1939, the Allies consisted of Poland, the United Kingdom, and France as well as their dependent states, such as British India. 
Axis Powers 
The Axis powers, originally called the Rome–Berlin Axis was a military coalition that fought in World War II against the Allies. The Axis powers agreed on their opposition to the Allies, but did not completely coordinate their activity. The Axis grew out of the diplomatic efforts of Nazi Germany, the Kingdom of Italy, and the Empire of Japan to secure their own specific expansionist interests in the mid-1930s. 
Pearl Harbor 
Pearl Harbor is an American lagoon harbor on the island of Oahu, Hawaii, west of Honolulu. It has been long visited by the Naval fleet of the United States, before it was acquired from the Hawaiian Kingdom by the U.S. with the signing of the Reciprocity Treaty of 1875. Much of the harbor and surrounding lands are now a United States Navy deep-water naval base. 
D-Day 
The Normandy landings were the landing operations and associated airborne operations on Tuesday, 6 June 1944 of the Allied invasion of Normandy in Operation Overlord during World War II. Codenamed Operation Neptune and often referred to as D-Day, it was the largest seaborne invasion in history. The operation began the liberation of France (and later western Europe) and laid the foundations of the Allied victory on the Western Front. Planning for the operation began in 1943. 
Fall of Berlin - 1945 
Fall of Berlin – 1945, The Fall of Berlin, or just Berlin (Russian: Берлин) is a Soviet documentary film about the Battle of Berlin, titled in Russian Битва за Берлин 1945 г., literally The Battle for Berlin – 1945. The film was directed by Yuli Raizman and Yelizaveta Svilova. The film begins with an animated map of Eastern Europe with Soviet soldier double exposed on the bottom. 
Battle of Midway 
The Battle of Midway was a major naval battle in the Pacific Theater of World War II that took place on 4–7 June 1942, six months after Japan’s attack on Pearl Harbor and one month after the Battle of the Coral Sea. The U.S. Navy under Admirals Chester W. Nimitz, Frank J. Fletcher, and Raymond A. Spruance defeated an attacking fleet of the Imperial Japanese Navy under Admirals Isoroku Yamamoto, Chūichi Nagumo, and Nobutake Kondō near Midway Atoll, inflicting devastating damage on the Japanese fleet that rendered their aircraft carriers irreparable. Military historian John Keegan called it "the most stunning and decisive blow in the history of naval warfare", while naval historian Craig Symonds called it "one of the most consequential naval engagements in world history, ranking alongside Salamis, Trafalgar, and Tsushima Strait, as both tactically decisive and strategically influential".The Japanese operation, like the earlier attack on Pearl Harbor, sought to eliminate the United States as a strategic power in the Pacific, thereby giving Japan a free hand in establishing its Greater East Asia Co-Prosperity Sphere. 
Manhattan Project 
The Manhattan Project was a research and development undertaking during World War II that produced the first nuclear weapons. It was led by the United States with the support of the United Kingdom (which initiated the original Tube Alloys project) and Canada. From 1942 to 1946, the project was under the direction of Major General Leslie Groves of the U.S. Army Corps of Engineers. 
Sonar 
Sonar (sound navigation and ranging) is a technique that uses sound propagation (usually underwater, as in submarine navigation) to navigate, communicate with or detect objects on or under the surface of the water, such as other vessels. Two types of technology share the name "sonar": passive sonar is essentially listening for the sound made by vessels; active sonar is emitting pulses of sounds and listening for echoes. Sonar may be used as a means of acoustic location and of measurement of the echo characteristics of "targets" in the water. 
Rationing 
Rationing is the controlled distribution of scarce resources, goods, services, or an artificial restriction of demand. Rationing controls the size of the ration, which is one's allowed portion of the resources being distributed on a particular day or at a particular time. There are many forms of rationing, and in western civilization people experience some of them in daily life without realizing it. Rationing is often done to keep price below the market-clearing price determined by the process of supply and demand in an unfettered market. 
Korematsu v. United States 
Korematsu v. United States, 323 U.S. 214 (1944), was a landmark United States Supreme Court case upholding the exclusion of Japanese Americans from the West Coast Military Area during World War II. The decision has widely been criticized, with some scholars describing it as "an odious and discredited artifact of popular bigotry" and as "a stain on American jurisprudence". Chief Justice John Roberts wrote in his majority opinion in the 2018 case of Trump v. 
United Nations 
The United Nations (UN) is an intergovernmental organization that aims to maintain international peace and security, develop friendly relations among nations, achieve international cooperation, and be a centre for harmonizing the actions of nations. It is the largest, most familiar, most internationally represented and most powerful intergovernmental organization in the world. The UN is headquartered on international territory in New York City, with its other main offices in Geneva, Nairobi, Vienna, and The Hague. 
Nuremberg Trials 
The Nuremberg trials (German: Nürnberger Prozesse) were a series of military tribunals held after World War II by the Allied forces under international law and the laws of war. The trials were most notable for the prosecution of prominent members of the political, military, judicial, and economic leadership of Nazi Germany, who planned, carried out, or otherwise participated in the Holocaust and other war crimes. The trials were held in Nuremberg, Germany, and their decisions marked a turning point between classical and contemporary international law. 
Clayton Anti-Trust Act 
The Clayton Antitrust Act of 1914 (Pub.L. 63–212, 38 Stat. 730, enacted October 15, 1914, codified at 15 U.S.C. §§ 12–27, 29 U.S.C. §§ 52–53), was a part of United States antitrust law with the goal of adding further substance to the U.S. antitrust law regime; the Clayton Act sought to prevent anticompetitive practices in their incipiency. That regime started with the Sherman Antitrust Act of 1890, the first Federal law outlawing practices considered harmful to consumers (monopolies, cartels, and trusts). 
Sherman Anti-Trust Act 
The Sherman Antitrust Act of 1890 (26 Stat. 209, 15 U.S.C. §§ 1–7) is a United States antitrust law that prescribes the rule of free competition among those engaged in commerce that was passed by Congress under the presidency of Benjamin Harrison. It is named for Senator John Sherman, its principal author. 
Robber Baron 
"Robber baron" is a derogatory term of social criticism originally applied to certain wealthy and powerful 19th-century American businessmen. The term appeared as early as the August 1870 issue of The Atlantic Monthly[1] magazine. By the late 1800s, the term was typically applied to businessmen who used exploitative practices to amass their wealth. 
Preservation Movement 
The conservation movement, also known as nature conservation, is a political, environmental, and social movement that seeks to manage and protect natural resources, including animal, fungus and plant species as well as their habitat for the future. Evidence-based conservation seeks to use high quality scientific evidence to make conservation efforts more effective. The early conservation movement included fisheries and wildlife management, water, soil conservation, and sustainable forestry 
1st New Deal 
The New Deal was a series of programs, public work projects, financial reforms, and regulations enacted by President Franklin D. Roosevelt in the United States between 1933 and 1939. Major federal programs and agencies included the Civilian Conservation Corps (CCC), the Civil Works Administration (CWA), the Farm Security Administration (FSA), the National Industrial Recovery Act of 1933 (NIRA) and the Social Security Administration (SSA). They provided support for farmers, the unemployed, youth and the elderly. 
2nd New Deal 
The New Deal was a series of programs, public work projects, financial reforms, and regulations enacted by President Franklin D. Roosevelt in the United States between 1933 and 1939. Major federal programs and agencies included the Civilian Conservation Corps (CCC), the Civil Works Administration (CWA), the Farm Security Administration (FSA), the National Industrial Recovery Act of 1933 (NIRA) and the Social Security Administration (SSA). They provided support for farmers, the unemployed, youth and the elderly. 
Relief, Recovery, Reform 
Recovery was the effort in numerous programs to restore the economy to normal health. By most economic indicators, this was achieved by 1937—except for unemployment, which remained stubbornly high until World War II began. Recovery was designed to help the economy bounce back from depression. Economic historians led by Price Fishback have examined the impact of New Deal spending on improving health conditions in the 114 largest cities, 1929–1937. They estimated that every additional $153,000 in relief spending (in 1935 dollars, or $1.95  million in the year 2000 dollars) was associated with a reduction of one infant death, one suicide, and 2.4 deaths from infectious disease. Relief was the immediate effort to help the one-third of the population that was hardest hit by the depression. Relief was also aimed at providing temporary help to suffering and unemployed Americans. Local and state budgets were sharply reduced because of falling tax revenue, but New Deal relief programs were used not just to hire the unemployed but also to build needed schools, municipal buildings, waterworks, sewers, streets, and parks according to local specifications. While the regular Army and Navy budgets were reduced, Roosevelt juggled relief funds to provide for their claimed needs. All of the CCC camps were directed by army officers, whose salaries came from the relief budget. The PWA built numerous warships, including two aircraft carriers; the money came from the PWA agency. PWA also built warplanes, while the WPA built military bases and airfields. Reform was based on the assumption that the depression was caused by the inherent instability of the market and that government intervention was necessary to rationalize and stabilize the economy and to balance the interests of farmers, business and labor. Reforms targeted the causes of the depression and sought to prevent a crisis like it from happening again. In other words, financially rebuilding the U.S. while ensuring not to repeat history. 
Limited Welfare State 
The welfare state is a form of government in which the state protects and promotes the economic and social well-being of the citizens, based upon the principles of equal opportunity, equitable distribution of wealth, and public responsibility for citizens unable to avail themselves of the minimal provisions for a good life.[1] Sociologist T. H. Marshall described the modern welfare state as a distinctive combination of democracy, welfare, and capitalism. As a type of mixed economy, the welfare state funds the governmental institutions for health care and education along with direct benefits given to individual citizens. 
Common National Culture 
National identity is a person's identity or sense of belonging to one state or to one nation.[1][2] It is the sense of "a nation as a cohesive whole, as represented by distinctive traditions, culture, and language."[3] National identity may refer to the subjective feeling one shares with a group of people about a nation, regardless of one's legal citizenship status. 
Restrictions on Civil Liberties 
Civil liberties are guarantees and freedoms that liberal governments commit not to abridge, either by legislation or judicial interpretation, without due process. Though the scope of the term differs between countries, civil liberties may include the freedom of conscience, freedom of press, freedom of religion, freedom of expression, freedom of assembly, the right to security and liberty, freedom of speech, the right to privacy, the right to equal treatment under the law and due process, the right to a fair trial, and the right to life. Other civil liberties include the right to own property, the right to defend oneself, and the right to bodily integrity. 
Scientific Modernist 
The Fundamentalist–Modernist controversy is a major schism that originated in the 1920s and '30s within the Presbyterian Church in the United States of America. At issue were foundational disputes about the role of Christianity, the authority of Scripture, the death, Resurrection, and atoning sacrifice of Jesus.[1] Two broad factions within Protestantism emerged: Fundamentalists, who insisted upon the timeless validity of each doctrine of Christian Orthodoxy, and Modernists, who advocated a conscious adaptation of religion in response to the new scientific discoveries and the moral pressures of the age. 
New Immigrants 
Immigration to the United States is the international movement of non-U.S. nationals in order to reside permanently in the country.[1] Immigration has been a major source of population growth and cultural change throughout much of the U.S. history. Because the United States is a settler colonial society, all Americans, with the exception of the small percentage of Native Americans, can trace their ancestry to immigrants from other nations around the world. 
Old Immigrants 
Immigration to the United States is the international movement of non-U.S. nationals in order to reside permanently in the country.[1] Immigration has been a major source of population growth and cultural change throughout much of the U.S. history. Because the United States is a settler colonial society, all Americans, with the exception of the small percentage of Native Americans, can trace their ancestry to immigrants from other nations around the world. 
National Origins Act of 1924 
The Immigration Act of 1924, or Johnson–Reed Act, including the Asian Exclusion Act and National Origins Act (Pub.L. 68–139, 43 Stat. 153, enacted May 26, 1924), was a United States federal law that prevented immigration from Asia, set quotas on the number of immigrants from the Eastern Hemisphere, and provided funding and an enforcement mechanism to carry out the longstanding ban on other immigrants. The 1924 act supplanted earlier acts to effectively ban all immigration from Asia[1][2] and set a total immigration quota of 165,000 for countries outside the Western Hemisphere, an 80% reduction from the average before World War I.[1] Quotas for specific countries were based on 2% of the US population from that country recorded in the 1890 census. 
Great Migration 
The Great Migration, sometimes known as the Great Northward Migration or the Black Migration, was the movement of 6 million African Americans out of the rural Southern United States to the urban Northeast, Midwest and West that occurred between 1916 and 1970.[1] It was caused primarily by the poor economic conditions as well as the prevalent racial segregation and discrimination in the Southern states where Jim Crow laws were upheld.[2][3] From the earliest U.S. population statistics in 1780 until 1910, more than 90% of the African-American population lived in the American South.[4][5][6] By the end of the Great Migration, just over half of the African-American population lived in the South, while a little less than half lived in the North and West. 
Great Depression Era Mexican Deportation 
The Great Depression began with the Wall Street Crash in October 1929. The stock market crash marked the beginning of a decade of high unemployment, poverty, low profits, deflation, plunging farm incomes, and lost opportunities for economic growth as well as for personal advancement. Altogether, there was a general loss of confidence in the economic future.[1] The usual explanations include numerous factors, especially high consumer debt, ill-regulated markets that permitted overoptimistic loans by banks and investors, and the lack of high-growth new industries. 
Anti-Imperialists 
Anti-imperialism in political science and international relations is a term used in a variety of contexts, usually by nationalist movements who want to secede from a larger polity[citation needed] (usually in the form of an empire, but also in a multi-ethnic sovereign state) or as a specific theory opposed to capitalism in Marxist–Leninist discourse, derived from Vladimir Lenin's work Imperialism, the Highest Stage of Capitalism. A less common usage is by supporters of a non-interventionist foreign policy. People who categorize themselves as anti-imperialists often state that they are opposed to colonialism, colonial empires, hegemony, imperialism and the territorial expansion of a country beyond its established borders. 
Wilson’s 14 Points 
The Fourteen Points was a statement of principles for peace that was to be used for peace negotiations in order to end World War I. The principles were outlined in a January 8, 1918, speech on war aims and peace terms to the United States Congress by President Woodrow Wilson. However, his main Allied colleagues (Georges Clemenceau of France, David Lloyd George of the United Kingdom, and Vittorio Orlando of Italy) were sceptical of the applicability of Wilsonian idealism.  
Neutrality Acts of 1935-1937 
The Neutrality Acts were a series of acts passed by the United States Congress in the 1930s (specifically 1935, 1936, 1937, and 1939) in response to the growing threats and wars that led to World War II. They were spurred by the growth in isolationism and non-interventionism in the US following its disillusionment after World War I, and sought to ensure that the US would not become entangled again in foreign conflicts. The legacy of the Neutrality Acts is widely regarded as having been generally negative; they made no distinction between aggressor and victim, treating both equally as belligerents, and they limited the US government's ability to aid Britain and France against Nazi Germany. 
Island Hopping 
Leapfrogging, also known as island hopping, was a military strategy employed by the Allies in the Pacific War against the Empire of Japan and the Axis powers during World War II.[citation needed][dubious – discuss] The key idea is to bypass heavily fortified enemy islands instead of trying to capture every island in sequence en route to a final target. The reasoning is that those islands can simply be cut off from their supply chains (leading to their eventual capitulation) rather than needing to be overwhelmed by superior force, thus speeding up progress and reducing losses of troops and material. 
Los Alamos 
Los Alamos National Laboratory (Los Alamos or LANL for short) is a United States Department of Energy national laboratory initially organized during World War II for the design of nuclear weapons as part of the Manhattan Project. It is a short distance northwest of Santa Fe, New Mexico, in the southwestern United States. Los Alamos was selected as the top-secret location for bomb design in late 1942 and officially commissioned the next year, under the management of University of California. 
Mass Mobilization 
Mass mobilization (also known as social mobilization or popular mobilization) refers to mobilization of civilian population as part of contentious politics. Mass mobilization is defined as a process that engages and motivates a wide range of partners and allies at national and local levels to raise awareness of and demand for a particular development objective through face-to-face dialogue. Members of institutions, community networks, civic and religious groups and others work in a coordinated way to reach specific groups of people for dialogue with planned messages. 
Factory Conversion 
Economic conversion, defence conversion, or arms conversion, is a technical, economic and political process for moving from military to civilian markets. Economic conversion takes place on several levels and can be applied to different organizations. In terms of levels (roughly corresponding to geographic scales), conversion can take place at the level of new innovation projects, divisions within multi-divisional firms, companies, and national economies.""" 
title7 = []
definition7 = []

splitted = unit7.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title7.append(z)
        print(z)
    elif i%2 == 0:
        definition7.append(z)

for i, z in zip(title7, definition7):
    if i == '':
        title7.remove(i)
    if z == '':
        definition7.remove(z)

content7 = dict(zip(title7, definition7))

unit8 = """Cold War	 
The Cold War was a period of geopolitical tension between the Soviet Union and the United States and their respective allies, the Eastern Bloc and the Western Bloc, after World War II. Historians do not fully agree on the dates, but the period is generally considered to span the 1947 Truman Doctrine to the 1991 dissolution of the Soviet Union. The term "cold" is used because there was no large-scale fighting directly between the two superpowers, but they each supported major regional conflicts known as proxy wars. The conflict was based around the ideological and geopolitical struggle for global influence by the two powers, following their temporary alliance and victory against Nazi Germany in 1945. 
Soviet Union (USSR)	 
The Soviet Union, officially the Union of Soviet Socialist Republics (USSR), was a federal socialist state in Northern Eurasia that existed from 1922 to 1991. Nominally a union of multiple national Soviet republics, it was a one-party state prior to 1990 governed by the Communist Party, with Moscow as its capital in its largest republic, the Russian SFSR. Other major urban centers were Leningrad (Russian SFSR), Kiev (Ukrainian SSR), Minsk (Byelorussian SSR), Tashkent (Uzbek SSR), Alma-Ata (Kazakh SSR) and Novosibirsk (Russian SFSR). It was the largest country in the world by surface area, spanning over 10,000 kilometers (6,200 mi) east to west across 11 time zones and over 7,200 kilometers (4,500 mi) north to south. 
NATO	 
The North Atlantic Treaty Organization (NATO, ; French: Organisation du traité de l'Atlantique nord, OTAN), also called the North Atlantic Alliance, is an intergovernmental military alliance between 30 European and North American countries. The organization implements the North Atlantic Treaty that was signed on 4 April 1949. NATO constitutes a system of collective defence whereby its independent member states agree to mutual defence in response to an attack by any external party. 
Warsaw Pact	 
The Warsaw Treaty Organization (WTO), officially the Treaty of Friendship, Cooperation and Mutual Assistance, commonly known as the Warsaw Pact (WP), was a collective defense treaty signed in Warsaw, Poland between the Soviet Union and seven other Eastern Bloc socialist republics of Central and Eastern Europe in May 1955, during the Cold War. The Warsaw Pact was the military complement to the Council for Mutual Economic Assistance (CoMEcon), the regional economic organization for the socialist states of Central and Eastern Europe. The Warsaw Pact was created in reaction to the integration of West Germany into NATO in 1955 per the London and Paris Conferences of 1954, but it is also considered to have been motivated by Soviet desires to maintain control over military forces in Central and Eastern Europe.The Warsaw Pact was established as a balance of power or counterweight to NATO. There was no direct military confrontation between them; instead, the conflict was fought on an ideological basis and in proxy wars. 
Iron curtain 
The Iron Curtain was a political boundary dividing Europe into two separate areas from the end of World War II in 1945 until the end of the Cold War in 1991. The term symbolizes the efforts by the Soviet Union (USSR) to block itself and its satellite states from open contact with the West and its allied states. On the east side of the Iron Curtain were the countries that were connected to or influenced by the Soviet Union, while on the west side were the countries that were NATO members or nominally neutral. 
Containment Policy	 
Containment is a geopolitical strategic foreign policy pursued by the United States. It is loosely related to the term cordon sanitaire which was later used to describe the geopolitical containment of the Soviet Union in the 1940s. The strategy of "containment" is best known as a Cold War foreign policy of the United States and its allies to prevent the spread of communism after the end of World War II. As a component of the Cold War, this policy was a response to the Soviet Union's move to increase communist influence in Eastern Europe, Asia, Africa, and Latin America. 
Truman Doctrine	 
The Truman Doctrine was an American foreign policy with the primary goal of containing Soviet geopolitical expansion during the Cold War. It was announced to Congress by President Harry S. Truman on March 12, 1947, and further developed on July 4, 1948, when he pledged to contain the communist uprisings in Greece and Turkey. Direct American military force was usually not involved, but Congress appropriated financial aid to support the economies and militaries of Greece and Turkey. 
Marshall Plan	 
The Marshall Plan (officially the European Recovery Program, ERP) was an American initiative passed in 1948 for foreign aid to Western Europe. The United States transferred over $12 billion (equivalent to $130 billion in 2019) in economic recovery programs to Western European economies after the end of World War II. Replacing an earlier proposal for a Morgenthau Plan, it operated for four years beginning on April 3, 1948. The goals of the United States were to rebuild war-torn regions, remove trade barriers, modernize industry, improve European prosperity, and prevent the spread of communism. 
Mao Zedong	 
Mao Zedong (; simplified Chinese: 毛泽东; traditional Chinese: 毛澤東; pinyin: Máo Zédōng; December 26, 1893 – September 9, 1976), also known as Chairman Mao, was a Chinese communist revolutionary who was the founder of the People's Republic of China (PRC), which he ruled as the chairman of the Chinese Communist Party from its establishment in 1949 until his death in 1976. Ideologically a Marxist–Leninist, his theories, military strategies, and political policies are collectively known as Maoism. Mao was the son of a prosperous peasant in Shaoshan, Hunan. 
Korean War	 
The Korean War (South Korean: Korean: 6.25 전쟁, 한국전쟁; Hanja: 韓國戰爭; RR: Yugio Jeonjaeng, Hanguk Jeonjaeng; North Korean: Korean: 조국해방전쟁; Hanja: 祖國解放戰爭; MR: Choguk haebang chŏnjaeng, "Fatherland Liberation War"; 25 June 1950 – 27 July 1953) was a war between North Korea (with the support of China and the Soviet Union) and South Korea (with the support of the United Nations, principally from the United States). The war began on 25 June 1950 when North Korea invaded South Korea following clashes along the border and insurrections in the south. The war ended unofficially on 27 July 1953 in an armistice. 
Vietnam War	 
The Vietnam War (Vietnamese: Chiến tranh Việt Nam), also known as the Second Indochina War, and in Vietnam as the Resistance War Against America (Vietnamese: Kháng chiến chống Mỹ) or simply the American War, was a conflict in Vietnam, Laos, and Cambodia from 1 November 1955 to the fall of Saigon on 30 April 1975. It was the second of the Indochina Wars and was officially fought between North Vietnam and South Vietnam. North Vietnam was supported by the Soviet Union, China, and other communist allies; South Vietnam was supported by the United States, South Korea, the Philippines, Australia, Thailand, and other anti-communist allies. 
Détente	 
Détente (French pronunciation: ​[detɑ̃t], French: "relaxation") is the relaxation of strained relations, especially political, by verbal communication. The term, in diplomacy, originates from around 1912 when France and Germany tried unsuccessfully to reduce tensions.Most often, the term is used for a phase of the Cold War. It was the policy of relaxing tensions between the Soviet Union and the West, as promoted by Richard Nixon, Henry Kissinger and Leonid Brezhnev, between 1969 and 1974. 
Tet Offensive	 
The Tet Offensive of 1968  (Vietnamese: Sự kiện Tết Mậu Thân 1968), or officially called The General Offensive and Uprising of Tet Mau Than 1968 (Vietnamese: Tổng tiến công và nổi dậy, Tết Mậu Thân 1968) was a major escalation and one of the largest military campaigns of the Vietnam War. It was launched on January 30, 1968 by forces of the Viet Cong (VC) and North Vietnamese People's Army of Vietnam (PAVN) against the forces of the South Vietnamese Army of the Republic of Vietnam (ARVN), the United States Armed Forces and their allies. It was a campaign of surprise attacks against military and civilian command and control centers throughout South Vietnam. 
Vietnam Protests	 
Protests against the Vietnam War took place in the 1960s and 1970s. The protests were part of a movement in opposition to United States involvement in the Vietnam War, and as such took place mainly in the U.S.  The first protests against U.S. involvement in Vietnam were in 1945, when United States Merchant Marine sailors condemned the U.S. government for the use of U.S. merchant ships to transport European troops to "subjugate the native population" of Vietnam.
Arms Race	 
An arms race  occurs when two or more nations compete in increases in military personnel and materiel. Simply defined as a competition between two or more states to have superior armed forces; a competition concerning production of weapons, the growth of a military, and the aim of superior military technology. The term is also used to describe any long-term escalating competitive situation where each competitor focuses on out-doing the others. 
Eisenhower	 
Dwight David "Ike" Eisenhower  GCS CCLH KC (; October 14, 1890 – March 28, 1969) was an American military officer and statesman who served as the 34th president of the United States from 1953 to 1961. During World War II, he became a five-star general in the Army and served as Supreme Commander of the Allied Expeditionary Force in Europe. He was responsible for planning and supervising the invasion of North Africa in Operation Torch in 1942–43 and the successful invasion of Normandy in 1944–45 from the Western Front. 
Massive Retaliation	 
Massive retaliation, also known as  a massive response or massive deterrence, is a military doctrine and nuclear strategy in which a state commits itself to retaliate in much greater force in the event of an attack.  In the event of an attack from an aggressor, a state would massively retaliate by using a force disproportionate to the size of the attack. The aim of massive retaliation is to deter another state from initially attacking. 
Suez Crisis	 
The Suez Crisis, or the Second Arab–Israeli war, also called the tripartite aggression (العدوان الثلاثي) in the Arab world and Sinai War in Israel, was an invasion of Egypt in late 1956 by Israel, followed by the United Kingdom and France. The aims were to regain Western control of the Suez Canal and to remove Egyptian president Gamal Abdel Nasser, who had just nationalised the canal. After the fighting had started, political pressure from the United States, the Soviet Union and the United Nations led to a withdrawal by the three invaders. 
Eisenhower Doctrine	 
The Eisenhower Doctrine was a policy enunciated by Dwight D. Eisenhower on January 5, 1957, within a "Special Message to the Congress on the Situation in the Middle East".  Under the Eisenhower Doctrine, a Middle Eastern country could request American economic assistance or aid from U.S. military forces if it was being threatened by armed aggression. Eisenhower singled out the Soviet threat in his doctrine by authorizing the commitment of U.S. forces "to secure and protect the territorial integrity and political independence of such nations, requesting such aid against overt armed aggression from any nation controlled by international communism." The phrase "international communism" made the doctrine much broader than simply responding to Soviet military action. 
Sputnik	 
Sputnik 1 (; "Satellite-1", or "PS-1", Простейший Спутник-1 or Prosteyshiy Sputnik-1, "Elementary Satellite 1") was the first artificial Earth satellite. The Soviet Union launched it into an elliptical low Earth orbit on 4 October 1957. It orbited for three weeks before its batteries died and then orbited silently for two months before it fell back into the atmosphere on the 25th December 1957. 
Space Race	 
The Space Race was an informal 20th-century competition between two Cold War rivals, the Soviet Union (USSR) and the United States (US), to achieve firsts in spaceflight capability. It had its origins in the ballistic missile-based nuclear arms race between the two nations following World War II. The technological advantage required to rapidly achieve spaceflight milestones was seen as necessary for national security, and mixed with the symbolism and ideology of the time. The Space Race led to pioneering efforts to launch artificial satellites, uncrewed space probes to the Moon, Venus, and Mars, and human spaceflight in low Earth orbit and to the Moon.The competition began in earnest on August 2, 1955, when the Soviet Union responded to the US announcement four days earlier of intent to launch artificial satellites for the International Geophysical Year, by declaring they would also launch a satellite "in the near future". 
Cuban Revolution	 
The Cuban Revolution (Spanish: Revolución cubana) was an armed revolt conducted by Fidel Castro's revolutionary 26th of July Movement and its allies against the military dictatorship of Cuban President Fulgencio Batista. The revolution began in July 1953, and continued sporadically until the rebels finally ousted Batista on 31 December 1958, replacing his government. 26 July 1953 is celebrated in Cuba as the Day of the Revolution (Dia de la Revolución). 
Bay of Pigs	 
The Bay of Pigs (Spanish: Bahía de los Cochinos) is an inlet of the Gulf of Cazones located on the southern coast of Cuba. By 1910, it was included in Santa Clara Province, and then instead to Las Villas Province by 1961, but in 1976, it was reassigned to Matanzas Province, when the original six provinces of Cuba were re-organized into 14 new Provinces of Cuba. The bay is historically important for the failed Bay of Pigs Invasion of 1961. 
Cuban Missile Crisis	 
The Cuban Missile Crisis, also known as the October Crisis of 1962 (Spanish: Crisis de Octubre), the Caribbean Crisis (Russian: Карибский кризис, tr. Karibsky krizis, IPA: [kɐˈrʲipskʲɪj ˈkrʲizʲɪs]), or the Missile Scare, was a 1 month, 4 days (16 October – 20 November 1962) confrontation between the United States and the Soviet Union which escalated into an international crisis when American deployments of missiles in Italy and Turkey were matched by Soviet deployments of similar ballistic missiles in Cuba. The confrontation is often considered the closest the Cold War came to escalating into a full-scale nuclear war.In response to the presence of American Jupiter ballistic missiles in Italy and Turkey, and the failed Bay of Pigs Invasion of 1961, Soviet First Secretary Nikita Khrushchev agreed to Cuba's request to place nuclear missiles on the island to deter a future invasion. 
Red Scare	 
A Red Scare is the promotion of a widespread fear of a potential rise of communism or anarchism by a society or state.  The term is most often used to refer to two periods in the history of the United States which are referred to by this name. The First Red Scare, which occurred immediately after World War I, revolved around a perceived threat from the American labor movement, anarchist revolution, and political radicalism. 
Alger Hiss	 
Alger Hiss (November 11, 1904 – November 15, 1996) was an American government official accused in 1948 of having spied for the Soviet Union in the 1930s. Statutes of limitations had expired for espionage, but he was convicted of perjury in connection with this charge in 1950. Before the trial Hiss was involved in the establishment of the United Nations, both as a U.S. State Department official and as a U.N. official. 
Rosenbergs	 
Julius Rosenberg and Ethel Rosenberg were American citizens who were convicted of spying on behalf of the Soviet Union. The couple was accused of providing top-secret information about radar, sonar, jet propulsion engines, and valuable nuclear weapon designs; at that time the United States was the only country in the world with nuclear weapons. Convicted of espionage in 1951, they were executed by the federal government of the United States in 1953 in the Sing Sing correctional facility in Ossining, New York, becoming the first American civilians to be executed for such charges and the first to suffer that penalty during peacetime.Other convicted co-conspirators were sentenced to prison, including Ethel's brother, David Greenglass (who had made a plea agreement), Harry Gold, and Morton Sobell. 
HUAC	 
The House Committee on Un-American Activities (HCUA), popularly dubbed the House Un-American Activities Committee (HUAC), and from 1969 onwards known as the House Committee on Internal Security, was an investigative committee of the United States House of Representatives. The HUAC was created in 1938 to investigate alleged disloyalty and subversive activities on the part of private citizens, public employees, and those organizations suspected of having fascist or  communist ties. When the House abolished the committee in 1975, its functions were transferred to the House Judiciary Committee. 
Smith Act	 
The Alien Registration Act, popularly known as the Smith Act, 76th United States Congress, 3d session, ch. 439, 54 Stat. 670, 18 U.S.C. § 2385 is a United States federal statute that was enacted on June 28, 1940. 
Joseph McCarthy	 
Joseph Raymond McCarthy (November 14, 1908 – May 2, 1957) was an American politician and attorney who served as a Republican U.S. Senator from the state of Wisconsin from 1947 until his death in 1957. Beginning in 1950, McCarthy became the most visible public face of a period in the United States in which Cold War tensions fueled fears of widespread communist subversion. He is known for alleging that numerous communists and Soviet spies and sympathizers had infiltrated the United States federal government, universities, film industry, and elsewhere. 
Vietnam War Protests	 
Protests against the Vietnam War took place in the 1960s and 1970s. The protests were part of a movement in opposition to United States involvement in the Vietnam War, and as such took place mainly in the U.S. 
Credibility Gap	 
Credibility gap is a term that came into wide use with journalism, political and public discourse in the United States during the 1960s and 1970s. At the time, it was most frequently used to describe public skepticism about the Lyndon B. Johnson administration's statements and policies on the Vietnam War. It was used in journalism as a euphemism for recognized lies told to the public by politicians. 
Draft (politics) 
In elections in the United States, political drafts are used to encourage or pressure a certain person to enter a political race, by demonstrating a significant groundswell of support for the candidate.  
Students for Democratic Society (SDS)	 
Students for a Democratic Society (SDS) was a national student activist organization in the United States during the 1960s, and was one of the principal representations of the New Left. Disdaining permanent leaders, hierarchical relationships and parliamentary procedure, the founders conceived of the organization as a broad exercise in "participatory democracy." From its launch in 1960 it grew rapidly in the course of the tumultuous decade with over 300 campus chapters and 30,000 supporters recorded nationwide by its last national convention in 1969. The organization splintered at that convention amidst rivalry between factions seeking to impose national leadership and direction, and disputing "revolutionary" positions on, among other issues, the Vietnam War and Black Power. 
Lincoln Memorial Protests	 
The Lincoln Memorial is a US national memorial built to honor the 16th President of the United States, Abraham Lincoln. It is on the western end of the National Mall in Washington, D.C., across from the Washington Monument, and is in the form of a neoclassical temple. The memorial's architect was Henry Bacon. 
Kent State Shootings	 
The Kent State shootings, also known as the May 4 massacre and the Kent State massacre, were the killings of four and wounding of nine other unarmed Kent State University students by the Ohio National Guard on May 4, 1970 in Kent, Ohio, 40 miles south of Cleveland. The killings took place during a peace rally opposing the expanding involvement of the Vietnam War into neutral Cambodia by United States military forces as well as protesting the National Guard presence on campus. The incident marked the first time that a student had been killed in an anti-war gathering in United States history. 
1968 DNC Riots	 
The 1968 Democratic National Convention was held August 26–29 at the International Amphitheatre in Chicago, Illinois, United States. As President Lyndon B. Johnson had announced he would not seek reelection, the purpose of the convention was to select a new presidential nominee for the Democratic Party. The keynote speaker was Senator Daniel Inouye (D-Hawaii). 
Vietnamization	 
Vietnamization was a policy of the Richard Nixon administration to end U.S. involvement in the Vietnam War through a program to  "expand, equip, and train South Vietnamese forces and assign to them an ever-increasing combat role, at the same time steadily reducing the number of U.S. combat troops". Brought on by the Viet Cong's Tet Offensive, the policy referred to U.S. combat troops specifically in the ground combat role, but did not reject combat by the U.S. Air Force, as well as the support to South Vietnam, consistent with the policies of U.S. foreign military assistance organizations. U.S. citizens' mistrust of their government that had begun after the offensive worsened with the release of news about U.S. soldiers massacring civilians at My Lai (1968), the invasion of Cambodia (1970), and the leaking of the Pentagon Papers (1971). 
Gulf of Tokin Resolution	 
The Gulf of Tonkin Resolution or the Southeast Asia Resolution, Pub.L. 88–408, 78 Stat. 384, enacted August 10, 1964, was a joint resolution that the United States Congress passed on August 7, 1964, in response to the Gulf of Tonkin incident. It is of historic significance because it gave U.S. President Lyndon B. Johnson authorization, without a formal declaration of war by Congress, for the use of conventional military force in Southeast Asia. 
War Powers Act	 
The War Powers Resolution (also known as the War Powers Resolution of 1973 or the War Powers Act) (50 U.S.C. 1541–1548) is a federal law intended to check the U.S. president's power to commit the United States to an armed conflict without the consent of the U.S. Congress. The resolution was adopted in the form of a United States congressional joint resolution. It provides that the president can send the U.S. Armed Forces into action abroad only by declaration of war by Congress, "statutory authorization," or in case of "a national emergency created by attack upon the United States, its territories or possessions, or its armed forces." The War Powers Resolution requires the president to notify Congress within 48 hours of committing armed forces to military action and forbids armed forces from remaining for more than 60 days, with a further 30-day withdrawal period, without congressional authorization for use of military force (AUMF) or a declaration of war by the United States. 
OPEC	 
The Organization of the Petroleum Exporting Countries (OPEC,  OH-pek) is an intergovernmental organization of 13 countries. Founded on 14 September 1960 in Baghdad by the first five members (Iran, Iraq, Kuwait, Saudi Arabia, and Venezuela), it has since 1965 been headquartered in Vienna, Austria, although Austria is not an OPEC member state. As of September 2018, the 13 member countries accounted for an estimated 44 percent of global oil production and 81.5 percent of the world's "proven" oil reserves, giving OPEC a major influence on global oil prices that were previously determined by the so-called "Seven Sisters" grouping of multinational oil companies. 
Yom Kippur War (1973)	 
The Yom Kippur War, Ramadan War, or October War (Hebrew: מלחמת יום הכיפורים‎, Milẖemet Yom HaKipurim, or מלחמת יום כיפור, Milẖemet Yom Kipur; Arabic: حرب أكتوبر‎, Ḥarb ʾUktōbar, or حرب تشرين, Ḥarb Tišrīn), also known as the 1973 Arab–Israeli War, was fought from October 6 to 25, 1973, by a coalition of Arab states led by Egypt and Syria against Israel. The war took place mostly in Sinai and the Golan—occupied by Israel during the 1967 Six-Day War—with some fighting in African Egypt and northern Israel. Egypt's initial war objective was to use its military to seize a foothold on the east bank of the Suez Canal and use this to negotiate the return of the rest of Sinai.The war began when the Arab coalition launched a joint surprise attack on Israeli positions, on Yom Kippur, a widely observed day of rest, fasting, and prayer in Judaism, which also occurred that year during the Muslim holy month of Ramadan. 
1970s Energy Crisis	 
The 1970s energy crisis occurred when the Western world, particularly the United States, Canada, Western Europe, Australia, and New Zealand, faced substantial petroleum shortages, real and perceived, as well as elevated prices. The two worst crises of this period were the 1973 oil crisis and the 1979 energy crisis, when the Yom Kippur War and the Iranian Revolution triggered interruptions in Middle Eastern oil exports.The crisis began to unfold as petroleum production in the United States and some other parts of the world peaked in the late 1960s and early 1970s. World oil production per capita began a long-term decline after 1979.The major industrial centers of the world were forced to contend with escalating issues related to petroleum supply. 
Department of Energy	 
A Ministry of Energy or Department of Energy is a government department in some countries that typically oversees the production of fuel and electricity; in the United States, however, it manages nuclear weapons development and conducts energy-related research and development. The person in charge of such a department is usually known as a Minister of Energy or Minister for Energy. 
Civil Rights Movement	 
The civil rights movement in the United States was a decades-long campaign by African Americans and their like-minded allies to end institutionalized racial discrimination, disenfranchisement and racial segregation in the United States. The movement has its origins in the Reconstruction era during the late 19th century, although it made its largest legislative gains in the mid-1960s after years of direct actions and grassroots protests. The social movement's major nonviolent resistance and civil disobedience campaigns eventually secured new protections in federal law for the human rights of all Americans. 
A. Philip Randolph	 
Asa Philip Randolph (April 15, 1889 – May 16, 1979) was an American labor unionist, civil rights activist, and socialist politician. In 1925, he organized and led the Brotherhood of Sleeping Car Porters, the first predominantly African-American labor union. In the early Civil Rights Movement and the Labor Movement, Randolph was a voice that would not be silenced. 
Martin Luther King Jr.	 
Martin Luther King Jr. (born Michael King Jr.; January 15, 1929 – April 4, 1968) was an African American Baptist minister and activist who became the most visible spokesperson and leader in the Civil Rights Movement  from 1955 until his assassination in 1968. King advanced civil rights through nonviolence and civil disobedience, inspired by his Christian beliefs and the nonviolent activism of Mahatma Gandhi. 
Jackie Robinson	 
Jack Roosevelt Robinson (January 31, 1919 – October 24, 1972) was an American professional baseball player who became the first African American to play in Major League Baseball (MLB) in the modern era. Robinson broke the baseball color line when he started at first base for the Brooklyn Dodgers on April 15, 1947. When the Dodgers signed Robinson, they heralded the end of racial segregation in professional baseball that had relegated black players to the Negro leagues since the 1880s. 
SNCC	 
The Student Nonviolent Coordinating Committee (SNCC, often pronounced  SNIK) was the principal channel of student commitment in the United States to the civil rights movement during the 1960s. Emerging in 1960 from the student-led sit-ins at segregated lunch counters in Greensboro, North Carolina, and Nashville, Tennessee, the Committee sought to coordinate and assist direct-action challenges to the civic segregation and political exclusion of African Americans. From 1962, with the support of the Voter Education Project, SNCC committed to the registration and mobilization of black voters in the Deep South. 
SCLC	 
The Southern Christian Leadership Conference (SCLC) is an African-American civil rights organization. SCLC is closely associated with its first president, Martin Luther King Jr., who had a large role in the American civil rights movement.  On January 10, 1957, following the Montgomery bus boycott victory against the white democracy and consultations with Bayard Rustin, Ella Baker, and others, Martin Luther King Jr. 
Brown v. Board of Education (1954)	 
Brown v. Board of Education of Topeka, 347 U.S. 483 (1954), was a landmark decision of the U.S. Supreme Court in which the Court ruled that U.S. state laws establishing racial segregation in public schools are unconstitutional, even if the segregated schools are otherwise equal in quality. Handed down on May 17, 1954, the Court's unanimous (9–0) decision stated that "separate educational facilities are inherently unequal", and therefore violate the Equal Protection Clause of the Fourteenth Amendment of the U.S. Constitution. 
Little Rock 9	 
The Little Rock Nine was a group of nine African American students enrolled in Little Rock Central High School in 1957. Their enrollment was followed by the Little Rock Crisis, in which the students were initially prevented from entering the racially segregated school by Orval Faubus, the Governor of Arkansas. They then attended after the intervention of President Dwight D. Eisenhower. 
Executive Order 9981	 
Executive Order 9981 was issued on July 26, 1948, by President Harry S. Truman. This executive order abolished discrimination "on the basis of race, color, religion or national origin" in the United States Armed Forces, and led to the end of segregation in the services during the Korean War (1950–1953). It was a crucial event in the post-World War II civil rights movement and a major achievement of Truman's presidency. 
Assassination of JFK	 
John Fitzgerald Kennedy, the 35th President of the United States, was assassinated on Friday, November 22, 1963, at 12:30 p.m. Central Standard Time in Dallas, Texas, while riding in a presidential motorcade through Dealey Plaza. Kennedy was riding with his wife Jacqueline, Texas Governor John Connally, and Connally's wife Nellie when he was fatally shot by former U.S. Marine Lee Harvey Oswald, firing in ambush from a nearby building. 
Civil Rights Act of 1964	 
The Civil Rights Act of 1964 (Pub.L. 88–352, 78 Stat. 241, enacted July 2, 1964) is a landmark civil rights and labor law in the United States that outlaws discrimination based on race, color, religion, sex, national origin, and later sexual orientation and gender identity. It prohibits unequal application of voter registration requirements, racial segregation in schools and public accommodations, and employment discrimination. 
Voting Rights Act of 1965	 
The Voting Rights Act of 1965 is a landmark piece of federal legislation in the United States that prohibits racial discrimination in voting. It was signed into law by President Lyndon B. Johnson during the height of the civil rights movement on August 6, 1965, and Congress later amended the Act five times to expand its protections. Designed to enforce the voting rights guaranteed by the Fourteenth and Fifteenth Amendments to the United States Constitution, the Act secured the right to vote for racial minorities throughout the country, especially in the South. 
Poll Taxes	 
A poll tax, also known as head tax or capitation, is a tax levied as a fixed sum on every liable individual.Head taxes were important sources of revenue for many governments from ancient times until the 19th century. In the United Kingdom, poll taxes were levied by the governments of John of Gaunt in the 14th century, Charles II in the 17th and Margaret Thatcher in the 20th century. In the United States, voting poll taxes (whose payment was a precondition to voting in an election) have been used to disenfranchise impoverished and minority voters (especially under Reconstruction).By their very nature, poll taxes are considered very regressive taxes, are usually very unpopular and have been implicated in many uprisings.The word "poll" is an archaic term for "head" or "top of the head". 
Literacy Tests	 
A literacy test assesses a person's literacy skills: their ability to read and write. Literacy tests have been administered by various governments to immigrants. In the United States, between the 1850s and 1960s, literacy tests were administered to prospective voters, and this had the effect of disenfranchising African Americans and others with diminished access to education. 
Malcolm X	 
Malcolm X (born Malcolm Little; May 19, 1925 – February 21, 1965) was an African American Muslim minister and human rights activist who was a popular figure during the civil rights movement. He is best known for his time spent as a vocal spokesman for the Nation of Islam. Malcolm spent his adolescence living in a series of foster homes or with relatives after his father's death and his mother's hospitalization. 
Black Panthers	 
The Black Panther Party (BPP), originally the Black Panther Party for Self-Defense, was a Black Power  political organization founded by college students Bobby Seale (Chairman) and Huey P. Newton in October 1966 in Oakland, California. The party was active in the United States from 1966 until 1982, with chapters in numerous major cities, and international chapters in the United Kingdom in the early 1970s, and in Algeria from 1969 to 1972. At its inception on October 15, 1966, the Black Panther Party's core practice was its open carry armed citizens' patrols ("copwatching") to monitor the behavior of officers of the Oakland Police Department and challenge police brutality in the city. 
Assassination of Robert F. Kennedy	 
On June 5, 1968, presidential candidate Robert F. Kennedy was mortally wounded shortly after midnight at the Ambassador Hotel in Los Angeles. Earlier that evening, the 42-year-old junior senator from New York was declared the winner in the South Dakota and California 1968 Democratic Party presidential primaries during the 1968 United States presidential election. He was pronounced dead at 1:44 a.m. 
Feminist Movement	 
The feminist movement (also known as the women's movement, or simply feminism) refers to a series of political campaigns for reforms on issues such as reproductive rights, domestic violence, maternity leave, equal pay, women's suffrage, sexual harassment, and sexual violence. The movement's priorities vary among nations and communities, and range from opposition to female genital mutilation in one country, to opposition to the glass ceiling in another. Feminism in parts of the Western world has gone through a series of waves. 
Betty Friedan	 
Betty Friedan ( February 4, 1921 – February 4, 2006) was an American feminist writer and activist. A leading figure in the women's movement in the United States, her 1963 book The Feminine Mystique is often credited with sparking the second wave of American feminism in the 20th century. In 1966, Friedan co-founded and was elected the first president of the National Organization for Women (NOW), which aimed to bring women "into the mainstream of American society now [in] fully equal partnership with men". 
The Feminine Mystique	 
The Feminine Mystique is a book by Betty Friedan that is widely credited with sparking the beginning of second-wave feminism in the United States. It was published on February 19, 1963 by W. W. Norton. In 1957, Friedan was asked to conduct a survey of her former Smith College classmates for their 15th anniversary reunion; the results, in which she found that many of them were unhappy with their lives as housewives, prompted her to begin research for The Feminine Mystique, conducting interviews with other suburban housewives, as well as researching psychology, media, and advertising. 
National Organization for Women (NOW)	 
The National Organization for Women (NOW) is an American feminist organization founded in 1966. The organization consists of 550 chapters in all 50 U.S. states and in Washington, D.C. sThere were many influences contributing to the rise of NOW. Such influences included the President's Commission on the Status of Women, Betty Friedan's 1963 book The Feminine Mystique, and passage and lack of enforcement of the Civil Rights Act of 1964 (prohibiting sexual discrimination).The President's Commission on the Status of Women was established in 1961 by John F. Kennedy, in hopes of providing a solution to female discrimination in education, work force, and Social Security. Kennedy appointed Eleanor Roosevelt as the head of the organization. 
Gloria Steinem	 
Gloria Marie Steinem (; born March 25, 1934) is an American feminist journalist and social political activist who became nationally recognized as a leader and a spokeswoman for the American feminist movement in the late 1960s and early 1970s.Steinem was a columnist for New York magazine, and a co-founder of Ms. magazine. In 1969, Steinem published an article, "After Black Power, Women's Liberation", which brought her to national fame as a feminist leader. 
Roe v. Wade (1973)	 
Roe v. Wade, 410 U.S. 113 (1973), was a landmark decision of the U.S. Supreme Court in which the Court ruled that the Constitution of the United States protects a pregnant woman's liberty to choose to have an abortion without excessive government restriction. It struck down many U.S. federal and state abortion laws, and prompted an ongoing national debate in the United States about whether and to what extent abortion should be legal, who should decide the legality of abortion, what methods the Supreme Court should use in constitutional adjudication, and what the role  of religious and moral views in the political sphere should be. 
Stonewall Riots	 
The Stonewall riots (also referred to as the Stonewall uprising or the Stonewall rebellion) were a series of spontaneous demonstrations by members of the gay (LGBT) community in response to a police raid that began in the early morning hours of June 28, 1969, at the Stonewall Inn in the Greenwich Village neighborhood of Manhattan, New York City. Patrons of the Stonewall, other Village lesbian and gay bars, and neighborhood street people fought back when the police became violent. The riots are widely considered to constitute one of the most important events leading to the gay liberation movement and the twentieth century fight for LGBT rights in the United States.Gay Americans in the 1950s and 1960s faced an anti-gay legal system. 
Cesar Chavez	 
César Estrada Chávez (Spanish pronunciation: [ˈsesaɾ esˈtɾaða ˈtʃaβes]; also ['sizəɹ ˈtʃavɛz] March 31, 1927 – April 23, 1993) was an American labor leader, community organizer, businessman, and Latino American civil rights activist. Along with Dolores Huerta, he co-founded the National Farm Workers Association (NFWA), which later merged with the Agricultural Workers Organizing Committee (AWOC) to become the United Farm Workers (UFW) labor union. Ideologically, his world-view combined leftist politics with Roman Catholic social teachings. 
United Farm Workers (UFW)	 
The United Farm Workers of America, or more commonly just United Farm Workers (UFW), is a labor union for farmworkers in the United States. It originated from the merger of two workers' rights organizations, the Agricultural Workers Organizing Committee (AWOC) led by organizer Larry Itliong, and the National Farm Workers Association (NFWA) led by César Chávez and Dolores Huerta. They became allied and transformed from workers' rights organizations into a union as a result of a series of strikes in 1965, when the mostly Filipino farmworkers of the AWOC in Delano, California, initiated a grape strike, and the NFWA went on strike in support. 
American Indian Movement (AIM)	 
The American Indian Movement (AIM) is a Native American grassroots movement founded in July 1968 in Minneapolis, Minnesota, initially centred in urban areas to address systemic issues of poverty and police brutality against Native Americans. AIM soon widened its focus from urban issues to include many Indigenous Tribal issues that Native American groups have faced due to settler colonialism of the Americas, such as treaty rights, high rates of unemployment, education, cultural continuity, and preservation of Indigenous cultures.The formation of AIM propagated as a result of the United States' Public Law 959 Indian Relocation Act of 1956, alongside Public Law 280, otherwise known as the Indian Termination Act. These policies were enacted by the United States Congress under congressional plenary power, causing almost seventy-percent of American Indians to leave their communal homelands and relocate to urban centers, many in hopes of finding economic sustainability. 
Bury My Heart at Wounded Knee	 
Bury My Heart at Wounded Knee: An Indian History of the American West is a 1970 non-fiction book by American writer Dee Brown that covers the history of Native Americans in the American West in the late nineteenth century. The book expresses details of the history of American expansionism from a point of view that is critical of its effects on the Native Americans. Brown describes Native Americans' displacement through forced relocations and years of warfare waged by the United States federal government. 
Lyndon Johnson	 
Lyndon Baines Johnson (; August 27, 1908 – January 22, 1973), often referred to by his initials LBJ, was an American politician who served as the 36th president of the United States from 1963 to 1969, and previously as 37th vice president from 1961 to 1963. He assumed the presidency following the assassination of President John F. Kennedy. A Democrat from Texas, Johnson was also a United States representative and later majority leader in the United States Senate. 
Great Society	 
The Great Society  was a set of domestic programs in the United States launched by Democratic President Lyndon B. Johnson in 1964–65. It was coined during a 1964 speech by President Lyndon B. Johnson at Ohio University and came to represent his domestic agenda.  The main goal was the total elimination of poverty and racial injustice. 
War on Poverty	 
The war on poverty is the unofficial name for legislation first introduced by United States President Lyndon B. Johnson during his State of the Union address on January 8, 1964. This legislation was proposed by Johnson in response to a national poverty rate of around nineteen percent.  The speech led the United States Congress to pass the Economic Opportunity Act, which established the Office of Economic Opportunity (OEO) to administer the local application of federal funds targeted against poverty. 
Rachel Carson’s Silent Spring	 
Silent Spring is an environmental science book by Rachel Carson. The book was published on September 27, 1962, documenting the adverse environmental effects caused by the indiscriminate use of pesticides. Carson accused the chemical industry of spreading disinformation, and public officials of accepting the industry's marketing claims unquestioningly. 
Clean Air Act (1963)	 
The Clean Air Act of 1963 (42 U.S.C. § 7401) is a United States federal law designed to control air pollution on a national level. It is one of the United States' first and most influential modern environmental laws, and one of the most comprehensive air quality laws in the world. As with many other major U.S. federal environmental statutes, it is administered by the U.S. Environmental Protection Agency (EPA), in coordination with state, local, and tribal governments. 
Clean Water Act (1972)	 
The Clean Water Act (CWA) is the primary federal law in the United States governing water pollution. Its objective is to restore and maintain the chemical, physical, and biological integrity of the nation's waters; recognizing the responsibilities of the states in addressing pollution and providing assistance to states to do so, including funding for publicly owned treatment works for the improvement of wastewater treatment; and maintaining the integrity of wetlands.The Clean Water Act was one of the United States' first and most influential modern environmental laws. Its laws and regulations are primarily administered by the U.S. Environmental Protection Agency (EPA) in coordination with state governments, though some of its provisions, such as those involving filling or dredging, are administered by the U.S. Army Corps of Engineers. 
Environmental Protection Agency (EPA)	 
The Environmental Protection Agency (EPA) is an independent executive agency of the United States federal government tasked with environmental protection matters. President Richard Nixon proposed the establishment of EPA on July 9, 1970; it began operation on December 2, 1970, after Nixon signed an executive order. The order establishing the EPA was ratified by committee hearings in the House and Senate. 
Earth Day	 
Earth Day is an annual event celebrated around the world on April 22 to demonstrate support for environmental protection. First celebrated in 1970, it now includes events coordinated globally by the Earth Day Network in more than 193 countries.In 1969 at a UNESCO Conference in San Francisco, peace activist John McConnell proposed a day to honor the Earth and the concept of peace, to first be celebrated on March 21, 1970, the first day of spring in the northern hemisphere. This day of nature's equipoise was later sanctioned in a proclamation written by McConnell and signed by Secretary General U Thant at the United Nations. 
Liberalism	 
Liberalism is a political and moral philosophy based on liberty, consent of the governed and equality before the law. Liberals espouse a wide array of views depending on their understanding of these principles, but they generally support free markets, free trade, limited government, individual rights (including civil rights and human rights), capitalism, democracy, secularism, gender equality, racial equality, internationalism, freedom of speech, freedom of the press and freedom of religion. Yellow is the political colour most commonly associated with liberalism.Liberalism became a distinct movement in the Age of Enlightenment, when it became popular among Western philosophers and economists. 
Great Society’s Anti-Poverty Programs (examples)	 
The Great Society  was a set of domestic programs in the United States launched by Democratic President Lyndon B. Johnson in 1964–65. It was coined during a 1964 speech by President Lyndon B. Johnson at Ohio University and came to represent his domestic agenda.  The main goal was the total elimination of poverty and racial injustice. 
Medicare (United States) 
Medicare is a national health insurance program in the United States, begun in 1966 under the Social Security Administration (SSA) and now administered by the Centers for Medicare and Medicaid Services (CMS). It primarily provides health insurance for Americans aged 65 and older, but also for some younger people with disability status as determined by the SSA, and people with end stage renal disease and amyotrophic lateral sclerosis (ALS or Lou Gehrig's disease). In 2018, according to the 2019 Medicare Trustees Report, Medicare provided health insurance for over 59.9 million individuals—more than 52 million people aged 65 and older and about 8 million younger people. 
Warren Court	 
The Warren Court was the period in the history of the Supreme Court of the United States during which Earl Warren served as Chief Justice. Warren replaced the deceased Fred M. Vinson as Chief Justice in 1953, and Warren remained in office until he retired in 1969. Warren was succeeded as Chief Justice by Warren Burger. 
Miranda v. Arizona 
Miranda v. Arizona, 384 U.S. 436 (1966), was a landmark decision of the U.S. Supreme Court in which the Court ruled that the Fifth Amendment to the U.S. Constitution restricts prosecutors from using a person's statements made in response to interrogation in police custody as evidence at their trial unless they can show that the person was informed of the right to consult with an attorney before and during questioning, and of the right against self-incrimination before police questioning, and that the defendant not only understood these rights, but voluntarily waived them.   Miranda was viewed by many as a radical change in American criminal law, since the Fifth Amendment was traditionally understood only to protect Americans against formal types of compulsion to confess, such as threats of contempt of court. 
Griswold v. Connecticut	 
Griswold v. Connecticut, 381 U.S. 479 (1965), was a landmark decision of the US Supreme Court in which the Court ruled that the Constitution of the United States protects the liberty of married couples to buy and use contraceptives without government restriction. The case involved a Connecticut "Comstock law" that prohibited any person from using "any drug, medicinal article or instrument for the purpose of preventing conception." The court held that the statute was unconstitutional, and that "the clear effect of [the Connecticut law ...] is to deny disadvantaged citizens ... 
Conservative Movement	 
Conservatism in the United States is a political and social philosophy. It characteristically shows respect for  American traditions, republicanism, and limited government; supports Judeo-Christian values, moral universalism, and individualism; is pro-capitalist and pro-business while opposing trade unions; advocates for a strong national defense, gun rights, free trade, American exceptionalism, and a defense of tradition and of Western culture from perceived threats posed by communism, socialism, and moral relativism.All major American political parties enshrine liberty as a core value. American conservatives generally consider individual liberty—within the bounds of conservative values—as the fundamental trait of democracy. 
Barry Goldwater	 
Barry Morris Goldwater (January 2, 1909 – May 29, 1998) was an American politician, statesman, businessman, soldier and author who was a five-term Senator from Arizona (1953–1965, 1969–1987) and the Republican Party nominee for president of the United States in 1964. Goldwater is the politician most often credited with having sparked the resurgence of the American conservative political movement in the 1960s. Despite his loss of the 1964 presidential election in a landslide, many political pundits and historians believe he laid the foundation for the conservative revolution to follow, as the grassroots organizatiion and conservative takeover of the Republican party began a long-term realignment in American politics would all help to bring about the "Reagan Revolution" of the 1980s. 
Stagflation	 
In economics, stagflation or recession-inflation is a situation in which the inflation rate is high, the economic growth rate slows, and unemployment remains steadily high. It presents a dilemma for economic policy, since actions intended to lower inflation may exacerbate unemployment. The term, a portmanteau of stagnation and inflation, is generally attributed to Iain Macleod, a British Conservative Party politician who became Chancellor of the Exchequer in 1970. 
Watergate Scandal	 
The Watergate scandal was a political scandal in the United States involving the administration of U.S. President Richard Nixon from 1971 to 1974 that led to Nixon's resignation. The scandal stemmed from the Nixon administration's continuous attempts to cover up its involvement in the June 17, 1972 break-in of the Democratic National Committee headquarters at the Washington, D.C. Watergate Office Building. After the five perpetrators were arrested, the press and the U.S. Justice Department connected the cash found on them at the time to the Nixon re-election campaign committee. 
Richard Nixon	 
Richard Milhous Nixon (January 9, 1913 – April 22, 1994) was the 37th president of the United States, serving from 1969 to 1974. A member of the Republican Party, Nixon previously served as the 36th vice president from 1953 to 1961, having risen to national prominence as a representative and senator from California. After five years in the White House that saw the conclusion to the U.S. involvement in the Vietnam War, détente with the Soviet Union and China, and the establishment of the Environmental Protection Agency, he became the only president to resign from the office, following the Watergate scandal. 
Gerald Ford	 
Gerald Rudolph Ford Jr. (; born Leslie Lynch King Jr.; July 14, 1913 – December 26, 2006) was an American politician and attorney who served as the 38th president of the United States from 1974 to 1977. A member of the Republican Party, Ford previously served as the 40th vice president of the United States from 1973 to 1974. 
Iranian Hostage Crisis	 
The Iran hostage crisis was a diplomatic standoff between the United States and Iran. Fifty-two American diplomats and citizens were held hostage after a group of militarized Iranian college students belonging to the Muslim Student Followers of the Imam's Line, who supported the Iranian Revolution, took over the U.S. Embassy in Tehran and seized hostages. The hostages were held for 444 days from November 4, 1979, to January 20, 1981. 
Jimmy Carter	 
James Earl Carter Jr. (born October 1, 1924) is an American politician, businessman, and philanthropist who served as the 39th president of the United States from 1977 to 1981. A member of the Democratic Party, he previously served as a Georgia State Senator from 1963 to 1967 and as the 76th governor of Georgia from 1971 to 1975. 
Equal Rights Amendment	 
The Equal Rights Amendment (ERA) is a proposed amendment to the United States Constitution designed to guarantee equal legal rights for all American citizens regardless of sex. It seeks to end the legal distinctions between men and women in matters of divorce, property, employment, and other matters. The first version of an ERA was written by Alice Paul and Crystal Eastman and introduced in Congress in December 1923.In the early history of the Equal Rights Amendment, middle-class women were largely supportive, while those speaking for the working class were often opposed, pointing out that employed women needed special protections regarding working conditions and employment hours. 
Phyllis Schlafly	 
Phyllis Stewart Schlafly (; born Phyllis McAlpin Stewart; August 15, 1924 – September 5, 2016) was an American attorney,  conservative activist and author. She held traditional conservative social and political views, opposed feminism, gay rights and abortion, and successfully campaigned against ratification of the Equal Rights Amendment to the U.S. Constitution. She was opposed in turn by moderates and liberals for her attitudes on sex, gender roles, homosexuality and a number of other issues. 
Affirmative Action	 
Affirmative action refers to a set of policies and practices within a government or organization seeking to increase the representation of particular groups based on their gender, race, sexuality, creed or nationality in areas in which they are underrepresented such as education and employment. Historically and internationally, support for affirmative action has sought to achieve goals such as bridging inequalities in employment and pay, increasing access to education, promoting diversity, and redressing apparent past wrongs, harms, or hindrances. The nature of affirmative action policies varies from region to region and exists on a spectrum from a hard quota to merely targeting encouragement for increased participation. 
Bakke v. University of California	 
Regents of the University of California v. Bakke, 438 U.S. 265 (1978), was a landmark decision by the Supreme Court of the United States. It upheld affirmative action, allowing race to be one of several factors in college admission policy. 
Kennedy-Nixon Debates		 
The 1960 United States presidential election was the 44th quadrennial presidential election. It was held on Tuesday, November 8, 1960. In a closely contested election, Democratic United States Senator John F. Kennedy defeated incumbent Vice President Richard Nixon, the Republican Party nominee. 
Private Sector	 
The private sector is the part of the economy, sometimes referred to as the citizen sector, which is owned by private groups, usually as a means of enterprise for profit, rather than being owned by the state.  The private sector employs most of the workforce in some countries. In private sector, activities are guided by the motive to earn money. 
Interstate Highway Act	 
The Federal Aid Highway Act of 1956, popularly known as the National Interstate and Defense Highways Act (Public Law 84-627), was enacted on June 29, 1956, when President Dwight D. Eisenhower signed the bill into law. With an original authorization of $25 billion for the construction of 41,000 miles (66,000 km) of the Interstate Highway System supposedly over a 10-year period, it was the largest public works project in American history through that time.The addition of the term "defense" in the act's title was for two reasons: First, some of the original cost was diverted from defense funds. Secondly, most U.S. Air Force bases have a direct link to the system. 
Baby boom	 
A baby boom is a period marked by a significant increase of birth rate. This demographic phenomenon is usually ascribed within certain geographical bounds of defined national and cultural populations. People born during these periods are often called baby boomers; however, some experts distinguish between those born during such demographic baby booms and those who identify with the overlapping cultural generations. 
Levittown	 
Levittown is the name of seven large suburban housing developments created in the United States by  William J. Levitt and his company Levitt & Sons. Built after World War II for returning veterans and their new families, the communities offered attractive alternatives to cramped central city locations and apartments. The Veterans Administration and the Federal Housing Administration (FHA) guaranteed builders that qualified veterans could buy housing for a fraction of rental costs. 
Sun Belt	 
The Sun Belt is a region of the United States generally considered to stretch across the Southeast and Southwest. Another rough definition of the region is the area south of the 36th parallel. Several climates can be found in the region — desert/semi-desert (California, Nevada, Arizona, New Mexico, Utah, and Texas), Mediterranean (California), humid subtropical  (Florida, Georgia, South Carolina, North Carolina, Texas, Louisiana, Mississippi, Alabama, Arkansas, and Tennessee), subtropical highland (high-altitude Appalachian Tennessee, Georgia, and South Carolina) and tropical (South Florida). 
Immigration and Nationality Act of 1965	 
The Immigration and Nationality Act of 1965, also known as the Hart–Celler Act, is a federal law passed by the 89th United States Congress and signed into law by President Lyndon B. Johnson. The law abolished the National Origins Formula, which had been the basis of U.S. immigration policy since the 1920s. The act removed de facto discrimination against Southern and Eastern Europeans, Asians, as well as other non-Northwestern European ethnic groups from American immigration policy. 
Rock and Roll	 
Rock and roll (often written as rock & roll, rock 'n' roll, or rock 'n roll) is a genre of popular music that evolved in the United States during the late 1940s and early 1950s. It originated from  black musical styles such as gospel, jump blues, jazz, boogie woogie, rhythm and blues, and country music. While rock and roll's formative elements can be heard in blues records from the 1920s, and in country records of the 1930s, the genre did not acquire its name until 1954.According to journalist Greg Kot, "rock and roll" refers to a style of popular music originating in the U.S. in the 1950s. 
Beat Movement (Beatniks)	 
Beatnik was a media stereotype prevalent throughout the late 1940s, 1950s to mid-1960s that displayed the more superficial aspects of the Beat Generation literary movement of the late 1940s and early to mid 1950s. Elements of the beatnik trope included pseudo-intellectualism, drug use, and a cartoonish depiction of real-life people along with the spiritual quest of Jack Kerouac's autobiographical fiction.  In 1948, Kerouac introduced the phrase "Beat Generation", generalizing from his social circle to characterize the underground, anticonformist youth gathering in New York at that time. 
The Affluent Society	 
The Affluent Society is a 1958 (4th edition revised 1984) book by Harvard economist John Kenneth Galbraith. The book sought to clearly outline the manner in which the post–World War II United States was becoming wealthy in the private sector but remained poor in the public sector, lacking social and physical infrastructure, and perpetuating income disparities. The book sparked much public discussion at the time. 
Counter-Culture (Hippies)
The "Me" generation is a term referring to Baby Boomers in the United States and the self-involved qualities that some people associate with it. The 1970s were dubbed the "Me decade" by writer Tom Wolfe; Christopher Lasch was another writer who commented on the rise of a culture of narcissism among the younger generation of that era. The phrase caught on with the general public, at a time when "self-realization" and "self-fulfillment" were becoming cultural aspirations to which young people supposedly ascribed higher importance than social responsibility. 
Truman’s Federal Employee Loyalty Program	 
President Harry S. Truman signed United States Executive Order 9835, sometimes known as the "Loyalty Order", on March 21, 1947. The order established the first general loyalty program in the United States, designed to root out communist influence in the U.S. federal government. Truman aimed to rally public opinion behind his Cold War policies with investigations conducted under its authority. 
“Black Power" 
The Black Power movement was a social movement motivated by a desire for safety and self-sufficiency that was not available inside redlined African American neighborhoods, Black Power activists founded Black-owned bookstores, food cooperatives, farms, media, printing presses, schools, clinics and ambulance services. The international impact of the movement includes the Black Power Revolution in Trinidad and Tobago.By the late 1960s, Black Power came to represent the demand for more immediate violent action to counter American white supremacy. Most of these ideas were influenced by Malcolm X's criticism of Martin Luther King Jr.'s peaceful protest methods. 
Jerry Falwell and Moral Majority	 
The Moral Majority was a prominent American political organization associated with the Christian right and Republican Party. It was founded in 1979 by Baptist minister Jerry Falwell Sr. and associates, and dissolved in the late 1980s. 
Focus on the Family
Focus on the Family (FOTF or FotF) is an American fundamentalist Christian organization founded in 1977 in Southern California by James Dobson, based in Colorado Springs, Colorado. It promotes social conservative views on public policy. The group is one of a number of evangelical parachurch organizations that rose to prominence in the 1980s.""" 
title8 = []
definition8 = []

splitted = unit8.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title8.append(z)
        print(z)
    elif i%2 == 0:
        definition8.append(z)

for i, z in zip(title8, definition8):
    if i == '':
        title8.remove(i)
    if z == '':
        definition8.remove(z)

content8 = dict(zip(title8, definition8))

unit9 = """Conservative Values	
Conservatism in the United States is a political and social philosophy which characteristically shows respect for  American traditions, republicanism, and limited government. It typically supports Judeo-Christian values, moral universalism, American exceptionalism, and individualism. It is generally pro-capitalist and pro-business while opposing trade unions. 
Ronald Reagan	
Ronald Wilson Reagan ( RAY-gən; February 6, 1911 – June 5, 2004) was an American politician who served as the 40th president of the United States from 1981 to 1989 and became a highly influential voice of modern conservatism. Prior to his presidency, he was a Hollywood actor and union leader before serving as the 33rd governor of California from 1967 to 1975. Reagan was raised in a low-income family in small towns of northern Illinois.
Conservative Era	
The Conservative Party, officially the Conservative and Unionist Party, and also known colloquially as the Tories, Tory Party, or simply the Conservatives, is a political party in the United Kingdom. Ideologically, the Conservatives sit on the centre-right of the political spectrum. The Conservatives have been in government since 2010 and as of 2019, hold an overall majority in the House of Commons with 365 Members of Parliament. 
Reaganomics	
Reaganomics (; a portmanteau of [Ronald] Reagan and economics attributed to Paul Harvey), or Reaganism, refers to the neoliberal economic policies promoted by U.S. President Ronald Reagan during the 1980s. These policies are commonly associated with and characterized as supply-side economics, trickle-down economics, or voodoo economics by opponents, while Reagan and his advocates preferred to call it free-market economics. The four pillars of Reagan's economic policy were to reduce the growth of government spending, reduce the federal income tax and capital gains tax, reduce government regulation, and tighten the money supply in order to reduce inflation.The results of Reaganomics are still debated. 
Trickle-Down Economics	 
Trickle-down economics, also known as trickle-down theory or the horse and sparrow theory, is the economic proposition that taxes on businesses and the wealthy in society should be reduced as a means to stimulate business investment in the short term and benefit society at large in the long term. In recent history, the term has been used by critics of supply-side economic policies, such as "Reaganomics". Whereas general supply-side theory favors lowering taxes overall, trickle-down theory more specifically targets taxes on the upper end of the economic spectrum. 
Inertia	 
Inertia is the resistance of any physical object to any change in its velocity. This includes changes to the object's speed, or direction of motion. An aspect of this property is the tendency of objects to keep moving in a straight line at a constant speed, when no forces act upon them. 
Bill Clinton	 
William Jefferson Clinton (né Blythe III; born August 19, 1946) is an American lawyer and politician who served as the 42nd president of the United States from 1993 to 2001. Prior to his presidency, he served as governor of Arkansas (1979–1981 and 1983–1992) and as attorney general of Arkansas (1977–1979). A member of the Democratic Party, Clinton was known as a New Democrat, and many of his policies reflected a centrist "Third Way" political philosophy. 
NAFTA	 
The North American Free Trade Agreement (NAFTA; Spanish: Tratado de Libre Comercio de América del Norte, TLCAN; French: Accord de libre-échange nord-américain, ALÉNA) was an agreement signed by Canada, Mexico, and the United States that created a trilateral trade bloc in North America. The agreement came into force on January 1, 1994, and superseded the 1988 Canada–United States Free Trade Agreement between the United States and Canada. The NAFTA trade bloc formed one of the largest trade blocs in the world by gross domestic product. 
Welfare Reform	 
Welfare reforms are changes in the operation of a given welfare system, with the goals of reducing the number of individuals dependent on government assistance, keeping the welfare systems affordable, and assisting recipients to become self-sufficient. Classical liberals and conservatives generally argue that welfare and other tax-funded services reduce incentives to work, exacerbate the free-rider problem, and intensify poverty. On the other hand, socialists generally criticize welfare reform because it usually minimizes the public safety net and strengthens the capitalist economic system. 
Acquitted	 
In common law jurisdictions, an acquittal certifies that the accused is free from the charge of an offense, as far as the criminal law is concerned. The finality of an acquittal is dependent on the jurisdiction. In some countries, such as the United States, an acquittal operates to bar the retrial of the accused for the same offense, even if new evidence surfaces that further implicates the accused. 
George Bush	 
George Walker Bush (born July 6, 1946) is an American politician and businessman who served as the 43rd president of the United States from 2001 to 2009. A member of the Republican Party, he had previously been the 46th governor of Texas from 1995 to 2000. He was born into the Bush family: his father, George H. W. Bush, was the 41st president of the United States from 1989 to 1993. 
2000 Election	 
This electoral calendar 2008 lists the national/federal direct elections held in 2008 in the de jure and de facto sovereign states and their dependent territories. Referendums are included, even though they are not elections. By-elections are not included. 
Electoral College	 
An electoral college is a set of electors who are selected to elect a candidate to particular offices. Often these represent different organizations, political parties or entities, with each organization, political party or entity represented by a particular number of electors or with votes weighted in a particular way. 
Computers
A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. Modern computers have the ability to follow generalized sets of operations, called programs. These programs enable computers to perform an extremely wide range of tasks. 
Globalization	 
Globalization, or globalisation (Commonwealth English; see spelling differences), is the process of interaction and integration among people, companies, and governments worldwide. Globalization has accelerated since the 18th century due to advances in transportation and communication technology. This increase in global interactions has caused a growth in international trade and the exchange of ideas and culture. 
Closing of Print Newspapers	 
A newspaper is a periodical publication containing written information about current events and is often typed in black ink with a white or gray background. Newspapers can cover a wide variety of fields such as politics, business, sports and art, and often include materials such as opinion columns, weather forecasts, reviews of local services, obituaries, birth notices, crosswords, editorial cartoons, comic strips, and advice columns. Most newspapers are businesses, and they pay their expenses with a mixture of subscription revenue, newsstand sales, and advertising revenue. 
Rust Belt	 
The Rust Belt is a region of the Northeastern and Midwestern United States that has been experiencing industrial decline starting around 1980. It is made up largely of the Great Lakes Megalopolis, though definitions vary. Rust refers to the deindustrialization, economic decline, population loss, and urban decay due to the shrinking of its once-powerful industrial sector, such as steel production, automobile manufacturing, and coal mining. 
Union Membership Decline	 
Labor unions in the United States are organizations that represent workers in many industries recognized under US labor law since the 1935 enactment of the National Labor Relations Act. Their activity today centers on collective bargaining over wages, benefits, and working conditions for their membership, and on representing their members in disputes with management over violations of contract provisions. Larger trade unions also typically engage in lobbying activities and electioneering at the state and federal level. 
Income Gap	 
There are wide varieties of economic inequality, most notably measured using the distribution of income (the amount of money people are paid) and the distribution of wealth (the amount of wealth people own). Besides economic inequality between countries or states, there are important types of economic inequality between different groups of people.Important types of economic measurements focus on wealth, income, and consumption. There are many methods for measuring economic inequality, with the Gini coefficient being a widely used one. 
Sun Belt		 
The Sun Belt is a region of the United States generally considered to stretch across the Southeast and Southwest. Another rough definition of the region is the area south of the 36th parallel. Several climates can be found in the region — desert/semi-desert (California, Nevada, Arizona, New Mexico, Utah, and Texas), Mediterranean (California), humid subtropical  (Florida, Georgia, South Carolina, North Carolina, Texas, Louisiana, Mississippi, Alabama, Arkansas, and Tennessee), subtropical highland (high-altitude Appalachian Tennessee, Georgia, and South Carolina) and tropical (South Florida). 
Immigration Reform and Control Act (1986)	 
The Immigration Reform and Control Act (IRCA or the Simpson–Mazzoli Act) was passed by the 99th United States Congress and signed into law by U.S. President Ronald Reagan on November 6, 1986. The Immigration Reform and Control Act altered U.S. immigration law by making it illegal to hire illegal immigrants knowingly and establishing financial and other penalties for companies that employed illegal immigrants. The act also legalized most undocumented immigrants who had arrived in the country prior to January 1, 1982. 
Don’t Ask, Don’t Tell	 
"Don't ask, don't tell" (DADT) was the official United States policy on military service by gay men, bisexuals, and lesbians, instituted by the Clinton Administration. The policy was issued under Department of Defense Directive 1304.26 on December 21, 1993, and was in effect from February 28, 1994, until September 20, 2011. The policy prohibited military personnel from discriminating against or harassing closeted homosexual or bisexual service members or applicants, while barring openly gay, lesbian, or bisexual persons from military service. 
Nuclear Family	 
A nuclear family, elementary family or conjugal family is a family group consisting of two parents and their children (one or more). It is in contrast to a single-parent family, the larger extended family, or a family with more than two parents. Nuclear families typically center on a married couple which may have any number of children. 
Camp David Accords	 
The Camp David Accords were a pair of political agreements signed by Egyptian President Anwar Sadat and Israeli Prime Minister Menachem Begin on 17 September 1978, following twelve days of secret negotiations at Camp David, the country retreat of the President of the United States in Maryland. The two framework agreements were signed at the White House and were witnessed by President Jimmy Carter. The second of these frameworks (A Framework for the Conclusion of a Peace Treaty between Egypt and Israel) led directly to the 1979 Egypt–Israel peace treaty. 
Iran-Contra Affair	 
The Iran–Contra affair (Persian: ماجرای ایران-کنترا‎, Spanish: Caso Irán–Contra), popularized in Iran as the McFarlane affair, the Iran–Contra scandal, or simply Iran–Contra, was a political scandal in the United States that occurred during the second term of the Reagan Administration. Senior administration officials secretly facilitated the sale of arms to the Khomeini government of the Islamic Republic of Iran, which was the subject of an arms embargo. The administration hoped to use the proceeds of the arms sale to fund the Contras in Nicaragua. 
Oliver North	 
Oliver Laurence North (born October 7, 1943) is an American political commentator, television host, military historian, author, and retired United States Marine Corps lieutenant colonel. A veteran of the Vietnam War, North was a National Security Council staff member during the Iran–Contra affair, a political scandal of the late 1980s. It involved the illegal sale of weapons to the Khomeini government of the Islamic Republic of Iran to encourage the release of American hostages then held in Lebanon. 
Grenada	 
Grenada ( (listen) grə-NAY-də; Grenadian Creole French: Gwenad) is a country in the West Indies in the Caribbean Sea at the southern end of the Grenadines island chain. Grenada consists of the island of Grenada itself, two smaller islands, Carriacou and Petite Martinique, and several small islands which lie to the north of the main island and are a part of the Grenadines. It is located northwest of Trinidad and Tobago, northeast of Venezuela and southwest of Saint Vincent and the Grenadines. 
ICBMs	 
An intercontinental ballistic missile (ICBM) is a missile with a minimum range of 5,500 kilometres (3,400 mi) primarily designed for nuclear weapons delivery (delivering one or more thermonuclear warheads). Similarly, conventional, chemical, and biological weapons can also be delivered with varying effectiveness, but have never been deployed on ICBMs. Most modern designs support multiple independently targetable reentry vehicles (MIRVs), allowing a single missile to carry several warheads, each of which can strike a different target. 
Star Wars	 
Star Wars is an American epic space opera media franchise created by George Lucas, which began with the eponymous 1977 film and quickly became a worldwide pop-culture phenomenon. The franchise has been expanded into various films and other media, including television series, video games, novels, comic books, theme park attractions, and themed areas, comprising an all-encompassing fictional universe. In 2020, its total value was estimated at US$70 billion, and it is currently the fifth-highest-grossing media franchise of all time. 
“Tear Down That Wall” Speech	 
"Mr. Gorbachev, tear down this wall", also known as the Berlin Wall Speech, was a speech delivered by United States President Ronald Reagan in West Berlin on June 12, 1987. Reagan called for the General Secretary of the Communist Party of the Soviet Union, Mikhail Gorbachev, to open the Berlin Wall, which had separated West and East Berlin since 1961. 
Mikhail Gorbachev	 
Mikhail Sergeyevich Gorbachev (born 2 March 1931) is a Russian and former Soviet politician. The eighth and last leader of the Soviet Union, he was the General Secretary of the Communist Party of the Soviet Union from 1985 until 1991. He was also the country's head of state from 1988 until 1991, serving as the chairman of the Presidium of the Supreme Soviet from 1988 to 1989, chairman of the Supreme Soviet from 1989 to 1990, and president of the Soviet Union from 1990 to 1991. 
Collapse of Berlin Wall	 
The Berlin Wall (German: Berliner Mauer, pronounced [bɛʁˌliːnɐ ˈmaʊ̯ɐ] (listen)) was a guarded concrete barrier that physically and ideologically divided Berlin from 1961 to 1989. Construction of the wall was commenced by the German Democratic Republic (GDR, East Germany) on 13 August 1961. The Wall cut off West Berlin from surrounding East Germany, including East Berlin. 
End of Cold War	 
The Cold War period of 1985–1991 began with the rise of Mikhail Gorbachev as General Secretary of the Communist Party of the Soviet Union.  Gorbachev was a revolutionary leader for the USSR, as he was the first to promote liberalization of the political landscape (Glasnost) and the economy (Perestroika); prior to this, the USSR had been strictly prohibiting liberal reform and maintained an inefficient command economy.  The USSR, despite facing massive economic difficulties, was involved in a costly arms race with the United States under President Ronald Reagan. 
Persian Gulf War	 
The Gulf War (2 August 1990 – 28 February 1991) was a war waged by coalition forces from 35 nations led by the United States against Iraq in response to Iraq's invasion and annexation of Kuwait arising from oil pricing and production disputes. It was codenamed Operation Desert Shield (2 August 1990 – 17 January 1991) for operations leading to the buildup of troops and defense of Saudi Arabia and Operation Desert Storm (17 January 1991 – 28 February 1991) in its combat phase. On 2 August 1990, the Iraqi Army invaded and occupied Kuwait, which was met with international condemnation and brought immediate economic sanctions against Iraq by members of the UN Security Council. 
Sadaam Hussein	 
Saddam Hussein Abd al-Majid al-Tikriti (; Arabic: صدام حسين عبد المجيد التكريتي Ṣaddām Ḥusayn ʿAbd al-Maǧīd al-Tikrītī; 28 April 1937 – 30 December 2006) was an Iraqi politician who served as the fifth President of Iraq from 16 July 1979 until 9 April 2003. A leading member of the revolutionary Arab Socialist Ba'ath Party, and later, the Baghdad-based Ba'ath Party and its regional organization, the Iraqi Ba'ath Party—which espoused Ba'athism, a mix of Arab nationalism and Arab socialism—Saddam played a key role in the 1968 coup (later referred to as the 17 July Revolution) that brought the party to power in Iraq. As vice president under the ailing General Ahmed Hassan al-Bakr, and at a time when many groups were considered capable of overthrowing the government, Saddam created security forces through which he tightly controlled conflicts between the government and the armed forces. 
Global Warming	 
Climate change includes both global warming driven by human emissions of greenhouse gases and the resulting large-scale shifts in weather patterns. Though there have been previous periods of climatic change, since the mid-20th century humans have had an unprecedented impact on Earth's climate system and caused change on a global scale.The largest driver of warming is the emission of greenhouse gases, of which more than 90% are carbon dioxide (CO2) and methane. Fossil fuel burning (coal, oil, and natural gas) for energy consumption is the main source of these emissions, with additional contributions from agriculture, deforestation, and manufacturing. 
Al Gore	 
Albert Arnold Gore Jr. (born March 31, 1948) is an American politician and environmentalist who served as the 45th vice president of the United States from 1993 to 2001. Gore was Bill Clinton's running mate in their successful campaign in 1992 and the pair were re-elected in 1996. 
An Inconvenient Truth	 
An Inconvenient Truth is a 2006 American concert/documentary film directed by Davis Guggenheim about former United States Vice President Al Gore's campaign to educate people about global warming. The film features a slide show that, by Gore's own estimate, he has presented over 1,000 times to audiences worldwide. The idea to document Gore's efforts came from producer Laurie David, who saw his presentation at a town hall meeting on global warming, which coincided with the opening of The Day After Tomorrow. 
George W. Bush	 
George Walker Bush (born July 6, 1946) is an American politician and businessman who served as the 43rd president of the United States from 2001 to 2009. A member of the Republican Party, he had previously been the 46th governor of Texas from 1995 to 2000. He was born into the Bush family: his father, George H. W. Bush, was the 41st president of the United States from 1989 to 1993. 
9/11	 
The September 11 attacks, often referred to as 9/11, were a series of four coordinated terrorist attacks by the Wahhabi terrorist group Al-Qaeda against the United States on the morning of Tuesday, September 11, 2001. The attacks resulted in 2,977 fatalities, over 25,000 injuries, and substantial long-term health consequences, in addition to at least $10 billion in infrastructure and property damage. It is the deadliest terrorist attack in human history and the single  deadliest incident for firefighters and law enforcement officers in the history of the United States, with 340 and 72 killed, respectively. 
Al Qaeda	 
Al-Qaeda (; Arabic: القاعدة‎ al-Qāʿidah, IPA: [ælqɑːʕɪdɐ], translation: "The Base", "The Foundation", alternatively spelled al-Qaida and al-Qa'ida) is a militant Sunni Islamist multi-national organization founded in 1988 by Osama bin Laden, Abdullah Azzam, and several other Arab volunteers during the Soviet–Afghan War.Al-Qaeda operates as a network of Islamic extremists and Salafist jihadists. Al Qaeda’s long-term plans included the creation of a unified and global caliphate. The organization was founded by Emir Osama bin Laden, whose undisguised goal was to become a strong state under the banner of the caliphate. 
Osama bin Laden	 
Osama bin Mohammed bin Awad bin Laden  (Arabic: أسا‌مة بن محمد بن عو‌ض بن لا‌د‌ن‎, Usāmah bin Muḥammad bin Awaḍ bin Lādin; March 10, 1957 – May 2, 2011), also rendered Usama bin Ladin, was a founder of the pan-Islamic militant organization al-Qaeda, designated as a terrorist group by the United Nations Security Council, the North Atlantic Treaty Organization (NATO), the European Union, and various countries. He was a Saudi Arabian citizen until 1994 and a member of the wealthy bin Laden family. Bin Laden's father was Mohammed bin Awad bin Laden, a Saudi millionaire from Hadhramaut, Yemen, and the founder of the construction company, Saudi Binladin Group. 
Patriot Act (2001)	 
The USA PATRIOT Act (commonly known as the Patriot Act) is an Act of the United States Congress that was signed into law by U.S. President George W. Bush on October 26, 2001. USA PATRIOT is a backronym that stands for Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism.The Patriot Act was enacted following the September 11 attacks in an effort to dramatically tighten U.S. national security, particularly as it related to foreign terrorism. In general, the act included three main provisions:  expanded abilities of law enforcement to surveil, including by tapping domestic and international phones; eased interagency communication to allow federal agencies to more effectively use all available resources in counterterrorism efforts; and increased penalties for terrorism crimes and an expanded list of activities which would qualify someone to be charged with terrorism. 
War on Terror	 
The war on terror, also known as the Global War on Terrorism and U.S. War on Terror, is an international military campaign launched by the United States government after the September 11 attacks. The targets of the campaign are primarily Sunni Islamic fundamentalist armed groups located throughout the Muslim world, with the most prominent groups being Al-Qaeda, the Islamic State, the Taliban, Tehrik-i-Taliban Pakistan, and the various franchise groups of the former two organizations. The naming of the campaign uses a metaphor of war to refer to a variety of actions that do not constitute a specific war as traditionally defined. 
Afghanistan	 
Afghanistan ( (listen); Pashto/Dari: افغانستان, Pashto: Afġānistān pashto [avɣɒnisˈtɒn, ab-], Dari: Afġānestān [avɣɒnesˈtɒn]), officially the Islamic Republic of Afghanistan, is a landlocked country at the crossroads of Central and South Asia. Afghanistan is bordered by Pakistan to the east and south; Iran to the west; Turkmenistan, Uzbekistan, and Tajikistan to the north; and China to the northeast. Occupying 652,000 square kilometers (252,000 sq mi), it is a mountainous country with plains in the north and southwest. 
Taliban	 
The Taliban (Pashto: طالبان‎, romanized: ṭālibān, lit. 'students') or Taleban, who refer to themselves as the Islamic Emirate of Afghanistan (IEA), are a Sunni Islamic fundamentalist political movement and military organisation in Afghanistan currently waging war (an insurgency, or jihad) within that country. Since 2016, the Taliban's leader is Mawlawi Hibatullah Akhundzada.From 1996 to 2001, the Taliban held power over roughly three quarters of Afghanistan, and enforced a strict interpretation of Sharia, or Islamic law. 
War in Iraq	 
The Iraq War was a protracted armed conflict that began in 2003 with the invasion of Iraq by a United States-led coalition that overthrew the government of Saddam Hussein. The conflict continued for much of the next decade as an insurgency emerged to oppose the occupying forces and the post-invasion Iraqi government. An estimated 151,000 to 1,033,000 Iraqis were killed in the first three to four years of conflict. 
WMDs	 
A weapon of mass destruction (WMD) is a nuclear, radiological, chemical, biological, or any other weapon that can kill and bring significant harm to numerous humans or cause great damage to human-made structures (e.g., buildings), natural structures (e.g., mountains), or the biosphere. The scope and usage of the term has evolved and been disputed, often signifying more politically than technically. Originally coined in reference to aerial bombing with chemical explosives during World War II, it has later come to refer to large-scale weaponry of other technologies, such as chemical, biological, radiological, or nuclear warfare. 
Barack Obama	
Barack Hussein Obama II ( (listen) bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician and attorney who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004. 
Glass Stegall Act
The Glass–Steagall legislation describes four provisions of the United States Banking Act of 1933 separating commercial and investment banking.[1] The article 1933 Banking Act describes the entire law, including the legislative history of the provisions covered herein. As for the Glass–Steagall Act of 1932, the common name comes from the names of the Congressional sponsors, Senator Carter Glass and Representative Henry B. Steagall.[2] 
Clinton Impeachment
The impeachment of Bill Clinton occurred when Bill Clinton, the 42nd president of the United States, was impeached by the United States House of Representatives of the 105th United States Congress on December 19, 1998 for "high crimes and misdemeanors". The House adopted two articles of impeachment against Clinton, with the specific charges against Clinton were lying under oath and obstruction of justice. Two other articles had been considered, but rejected by House vote."""

title9 = []
definition9 = []

splitted = unit9.split("\n")
for i, z in zip(range(-1, len(splitted)), splitted):
    if (i%2) != 0:
        title9.append(z)
        print(z)
    elif i%2 == 0:
        definition9.append(z)

for i, z in zip(title9, definition9):
    if i == '':
        title9.remove(i)
    if z == '':
        definition9.remove(z)

content9 = dict(zip(title9, definition9))

writer = open('vocabfulltermsandstuff.txt', 'w', encoding='utf-8')

writer.write(f'{content1}\n\n {content2}\n\n {content3}\n\n {content4}\n\n {content5}\n\n {content6}\n\n {content7}\n\n {content8}\n\n {content9}\n\n')

writer.close()

# regex to fix formatting on some vocab docs: \n^\s*$