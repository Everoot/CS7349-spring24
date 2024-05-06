# Project topics

### 1 **量子随机性在安全应用中的实际利用**: 探索量子随机性如何为生成高强度密码和安全密钥提供理想的基础，并分析现实世界中实现该技术的挑战和可能性。

### 研究背景和重要性

- **量子随机性简介**：首先介绍量子随机性的基本原理，解释它如何与传统的伪随机数生成器（PRNGs）不同。量子随机性利用量子力学的基本性质，如量子叠加和不确定性原理，产生真正的随机数。
- **密码学中的随机性需求**：阐述高强度密码和安全密钥生成中对随机性的需求，以及为什么量子随机性被认为是理想的随机数源。

### 技术应用与案例研究

- **量子随机数生成器（QRNGs）**：介绍量子随机数生成器的工作原理，包括目前市场上可用的QRNGs设备和技术。讨论这些设备如何利用量子效应产生随机数。
- **安全密钥生成**：具体说明如何利用量子随机性在密码学中生成安全密钥，包括量子密钥分发（QKD）的案例。
- **高强度密码生成**：探讨量子随机数在生成难以预测和破解的高强度密码中的应用，以及这对增强数据保护的潜在影响。

### 实现挑战和可能性

- **技术挑战**：分析实现量子随机数生成器和将量子随机性应用于安全领域的主要技术挑战，包括硬件要求、成本和可扩展性问题。
- **标准化和认证**：讨论发展标准化框架和认证过程以确保量子随机数生成器的安全性和可靠性的重要性。
- **实际应用的可能性**：基于当前技术发展和市场趋势，评估量子随机性在安全应用中的实际应用可能性和潜在市场。

### 结论和未来方向

- **总结**：概括量子随机性如何为生成高强度密码和安全密钥提供理想的基础，以及当前面临的挑战和限制。
- **未来研究方向**：提出未来研究可能的方向，包括技术创新、新的应用场景以及如何解决现有的技术和实施挑战。

[1]

J. Guskind and W. O. Krawec, ‘Semi-Quantum Random Number Generation’, in *2023 IEEE International Conference on Quantum Computing and Engineering (QCE)*, Bellevue, WA, USA: IEEE, Sep. 2023, pp. 1211–1219. doi: [10.1109/QCE57702.2023.00137](https://doi.org/10.1109/QCE57702.2023.00137).



[2]

M. Berta, O. Fawzi, and S. Wehner, ‘Quantum to Classical Randomness Extractors’, *IEEE Trans. Inform. Theory*, vol. 60, no. 2, pp. 1168–1192, Feb. 2014, doi: [10.1109/TIT.2013.2291780](https://doi.org/10.1109/TIT.2013.2291780).



[3]

A. Epishkina and K. Kogos, ‘Quantum random number generator for secure communications’, in *2016 International Siberian Conference on Control and Communications (SIBCON)*, Moscow, Russia: IEEE, May 2016, pp. 1–4. doi: [10.1109/SIBCON.2016.7491712](https://doi.org/10.1109/SIBCON.2016.7491712).



[4]

M. Xu *et al.*, ‘An Explicit Non-Malleable Extraction Scheme for Quantum Randomness Amplification With Two Untrusted Devices’, *IEEE Commun. Lett.*, vol. 22, no. 1, pp. 85–88, Jan. 2018, doi: [10.1109/LCOMM.2017.2766631](https://doi.org/10.1109/LCOMM.2017.2766631).



[5]

M. Njorbuenwu, B. Swar, and P. Zavarsky, ‘A Survey on the Impacts of Quantum Computers on Information Security’, in *2019 2nd International Conference on Data Intelligence and Security (ICDIS)*, South Padre Island, TX, USA: IEEE, Jun. 2019, pp. 212–218. doi: [10.1109/ICDIS.2019.00039](https://doi.org/10.1109/ICDIS.2019.00039).





### 2 **量子计算对现有加密协议的威胁与对策**: 研究量子计算技术如何威胁当前加密技术（如RSA和ECC），以及开发量子安全加密算法作为解决方案的可能路径。

“量子计算对现有加密协议的威胁与对策：研究量子计算技术如何威胁当前加密技术（如RSA和ECC），以及开发量子安全加密算法作为解决方案的可能路径”作为研究论文题目，将涉及对当前加密体系在量子计算时代面临的挑战进行深入分析，并探索后量子密码学的发展方向。以下是撰写这篇论文的一些建议和关键点：

### 研究背景和重要性

- **量子计算简介**：介绍量子计算的基本原理，包括量子比特、量子叠加、量子纠缠等概念，以及量子计算对计算能力的潜在提升。
- **现有加密技术回顾**：详细介绍当前广泛使用的加密技术，如RSA、ECC以及它们在网络安全和数据保护中的应用。

### 量子计算对加密技术的威胁

- **Shor算法和Grover算法**：解释Shor算法如何有效解决大数分解和离散对数问题，对RSA、ECC等公钥加密体系构成直接威胁；同时，讨论Grover算法提供的搜索加速可能如何影响对称加密算法的安全性。
- **加密体系的脆弱性分析**：基于量子算法，分析现有加密技术面临的具体威胁，包括加密强度降低和安全假设失效等问题。

### 量子安全加密算法的发展

- **后量子密码学**：介绍后量子密码学的概念，包括旨在抵抗量子计算攻击的加密技术，如格基密码学、哈希基加密和码基加密等。
- **量子密钥分发（QKD）**：讨论QKD的原理和实现，以及它如何提供理论上无条件的安全性，作为量子安全通信的一个实践例证。

### 实现挑战和可能性

- **技术和实践挑战**：分析实施后量子密码算法和量子密钥分发系统面临的主要技术挑战，包括标准化、兼容性和部署问题。
- **未来加密策略**：探索在量子计算日益发展的背景下，维护网络安全和数据保护的长期策略，包括加密算法的选择、系统设计的适应性和安全协议的更新。

### 结论和未来方向

- **总结**：概述量子计算对现有加密技术的威胁，以及后量子密码学在确保长期网络安全中的作用和挑战。
- **研究和发展方向**：提出未来在量子安全加密算法研究和实践中可能的方向，包括加密技术的创新、量子抗性测试和跨学科合作的重要性。

通过这个题目，你将能够探索量子计算技术对传统加密协议构成的威胁，以及如何通过发展新的加密技术和安全策略来应对这一挑战，对于理解量子时代的网络安全环境及其未来走向具有重要意义。





[1]

L. K. Grover, ‘A fast quantum mechanical algorithm for database search’, in *Proceedings of the twenty-eighth annual ACM symposium on Theory of computing - STOC ’96*, Philadelphia, Pennsylvania, United States: ACM Press, 1996, pp. 212–219. doi: [10.1145/237814.237866](https://doi.org/10.1145/237814.237866).



[2]

A. A. Saki, M. Alam, K. Phalak, A. Suresh, R. O. Topaloglu, and S. Ghosh, ‘A Survey and Tutorial on Security and Resilience of Quantum Computing’, in *2021 IEEE European Test Symposium (ETS)*, Bruges, Belgium: IEEE, May 2021, pp. 1–10. doi: [10.1109/ETS50041.2021.9465397](https://doi.org/10.1109/ETS50041.2021.9465397).



[3]

M. Njorbuenwu, B. Swar, and P. Zavarsky, ‘A Survey on the Impacts of Quantum Computers on Information Security’, in *2019 2nd International Conference on Data Intelligence and Security (ICDIS)*, South Padre Island, TX, USA: IEEE, Jun. 2019, pp. 212–218. doi: [10.1109/ICDIS.2019.00039](https://doi.org/10.1109/ICDIS.2019.00039).



[4]

A. Mandviwalla, K. Ohshiro, and B. Ji, ‘Implementing Grover’s Algorithm on the IBM Quantum Computers’, in *2018 IEEE International Conference on Big Data (Big Data)*, Seattle, WA, USA: IEEE, Dec. 2018, pp. 2531–2537. doi: [10.1109/BigData.2018.8622457](https://doi.org/10.1109/BigData.2018.8622457).



[5]

Z. S. Ageed, S. R. M. Zeebaree, and R. H. Saeed, ‘Influence of Quantum Computing on IoT Using Modern Algorithms’, in *2022 4th International Conference on Advanced Science and Engineering (ICOASE)*, Zakho, Iraq: IEEE, Sep. 2022, pp. 194–199. doi: [10.1109/ICOASE56293.2022.10075583](https://doi.org/10.1109/ICOASE56293.2022.10075583).
