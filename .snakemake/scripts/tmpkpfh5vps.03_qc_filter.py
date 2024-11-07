
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/opt/miniforge3/envs/scanpy/lib/python3.9/site-packages', '/home/mint/.cache/snakemake/snakemake/source-cache/runtime-cache/tmp5a87b0ly/file/mnt/exfat01/projects/scRNA-0722/workflow/scripts/scanpy', '/mnt/exfat01/projects/scRNA-0722/workflow/scripts/scanpy']); import pickle; snakemake = pickle.loads(b'\x80\x04\x95\x94\x08\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8c-data/processed/scanpy/02_normalized_data.h5ad\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x04h5ad\x94K\x00N\x86\x94s\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x12\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x18)}\x94\x8c\x05_name\x94h\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh\x0eh\nub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8c.data/processed/scanpy/03_qc_filtered_data.h5ad\x94a}\x94(h\x0c}\x94h\x0eK\x00N\x86\x94sh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bh\x0eh&ub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94(}\x94(\x8c\x10max_nFeature_RNA\x94M@\x1f\x8c\x10min_nFeature_RNA\x94M\xf4\x01\x8c\x0emax_nCount_RNA\x94M0u\x8c\x0emin_nCount_RNA\x94M\xe8\x03\x8c\x0emax_percent_mt\x94K\n\x8c\x10max_percent_ribo\x94K\x14\x8c\x0emin_num_Malat1\x94K\x03\x8c\x0emax_percent_hb\x94K\x01\x8c\x10percent_doublets\x94G?\xa9\x99\x99\x99\x99\x99\x9au}\x94(\x8c\x06seurat\x94\x8c\x0efigures/seurat\x94\x8c\x06scanpy\x94\x8c\x0efigures/scanpy\x94ue}\x94(h\x0c}\x94(\x8c\x02qc\x94K\x00N\x86\x94\x8c\x0bfigures_dir\x94K\x01N\x86\x94uh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bhHh7hJhAub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01\x8c\x04/tmp\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06tmpdir\x94K\x02N\x86\x94uh\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bhlK\x01hnK\x01hphiub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8c\x1clogs/scanpy/03_qc_filter.log\x94a}\x94(h\x0c}\x94h\x10]\x94(h\x12h\x13eh\x12h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x12sNt\x94bh\x13h\x16h\x18\x85\x94R\x94(h\x18)}\x94h\x1ch\x13sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x05input\x94}\x94(\x8c\x06seurat\x94\x8c\x19data/raw/seurat_input.rds\x94\x8c\x06scanpy\x94\x8c\x1adata/raw/scanpy_input.h5ad\x94u\x8c\noutput_dir\x94}\x94(\x8c\x06seurat\x94\x8c\x0eresults/seurat\x94\x8c\x06scanpy\x94\x8c\x0eresults/scanpy\x94u\x8c\rprocessed_dir\x94}\x94(\x8c\x06seurat\x94\x8c\x15data/processed/seurat\x94\x8c\x06scanpy\x94\x8c\x15data/processed/scanpy\x94u\x8c\x0bfigures_dir\x94hA\x8c\x02qc\x94h7\x8c\x0en_var_features\x94M\xc4\t\x8c\x10regress_features\x94]\x94(\x8c\nnCount_RNA\x94\x8c\x0cnFeature_RNA\x94\x8c\npercent.mt\x94\x8c\x0cpercent.ribo\x94\x8c\tG2m_score\x94\x8c\x07S_score\x94e\x8c\x05n_pcs\x94K\x1e\x8c\x0bresolutions\x94]\x94(K\x00G?\xc0\x00\x00\x00\x00\x00\x00G?\xd0\x00\x00\x00\x00\x00\x00G?\xd8\x00\x00\x00\x00\x00\x00G?\xe0\x00\x00\x00\x00\x00\x00G?\xe4\x00\x00\x00\x00\x00\x00G?\xe8\x00\x00\x00\x00\x00\x00G?\xec\x00\x00\x00\x00\x00\x00K\x01G?\xf2\x00\x00\x00\x00\x00\x00G?\xf4\x00\x00\x00\x00\x00\x00G?\xf6\x00\x00\x00\x00\x00\x00G?\xf8\x00\x00\x00\x00\x00\x00G?\xfa\x00\x00\x00\x00\x00\x00G?\xfc\x00\x00\x00\x00\x00\x00G?\xfe\x00\x00\x00\x00\x00\x00K\x02G@\x01\x00\x00\x00\x00\x00\x00G@\x02\x00\x00\x00\x00\x00\x00G@\x03\x00\x00\x00\x00\x00\x00G@\x04\x00\x00\x00\x00\x00\x00G@\x05\x00\x00\x00\x00\x00\x00G@\x06\x00\x00\x00\x00\x00\x00G@\x07\x00\x00\x00\x00\x00\x00K\x03e\x8c\x04umap\x94}\x94(\x8c\x04dims\x94K\x1e\x8c\x0bn_neighbors\x94K\x1e\x8c\x08min_dist\x94G?\xd9\x99\x99\x99\x99\x99\x9a\x8c\x06spread\x94K\x01\x8c\x06method\x94\x8c\numap-learn\x94\x8c\x06metric\x94\x8c\tminkowski\x94u\x8c\x07threads\x94K\x02\x8c\x0brandom_seed\x94K*\x8c\x07logging\x94}\x94(\x8c\x05level\x94\x8c\x04INFO\x94\x8c\x06output\x94\x8c\x11logs/analysis.log\x94uu\x8c\x04rule\x94\x8c\x10scanpy_qc_filter\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8c8/mnt/exfat01/projects/scRNA-0722/workflow/scripts/scanpy\x94ub.'); from snakemake.logging import logger; logger.printshellcmds = True; __real_file__ = __file__; __file__ = '/mnt/exfat01/projects/scRNA-0722/workflow/scripts/scanpy/03_qc_filter.py';
######## snakemake preamble end #########
import os
import scanpy as sc
import numpy as np
from snakemake.logging import logger

# 打印当前工作目录
current_working_directory = os.getcwd()
logger.info(f"当前工作目录: {current_working_directory}")

# 打印所有传递的命令行参数
input_file = snakemake.input[0]
output_file = snakemake.output[0]
qc_params = snakemake.params["qc"]
figures_dir = snakemake.params["figures_dir"]
logger.info(f"传递的参数:\n输入文件路径: {input_file}\n输出文件路径: {output_file}")
logger.info(f"QC 参数: {qc_params}")

try:
    # 从 H5AD 文件读取 AnnData 对象
    adata = sc.read_h5ad(input_file)
    logger.info(f"成功从以下路径读取 AnnData 对象: {input_file}")

    # 确认数据读取
    logger.info(f"AnnData 对象包含 {adata.n_obs} 行和 {adata.n_vars} 列的矩阵")
    logger.info(f"特征（变量）名称：{adata.var_names[:5]}")

    # 计算 QC 指标
    # 检查实际列名
    logger.info(f"数据中的列名: {adata.obs.columns.tolist()}")        

    percent_mt = np.sum(adata[:, adata.var_names.str.startswith("MT-")].X, axis=1) / adata.obs["nCount_RNA"] * 100
    percent_ribo = np.sum(adata[:, adata.var_names.str.startswith("RP")].X, axis=1) / adata.obs["nCount_RNA"] * 100
    percent_hb = np.sum(adata[:, adata.var_names.str.contains("HB")].X, axis=1) / adata.obs["nCount_RNA"] * 100

    adata.obs["percent.mt"] = percent_mt
    adata.obs["percent.ribo"] = percent_ribo
    adata.obs["percent.hb"] = percent_hb

    # 确认计算结果
    logger.info("计算的 QC 指标:")
    logger.info(f"前5行 percent.mt:\n{adata.obs['percent.mt'].head()}")
    logger.info(f"前5行 percent.ribo:\n{adata.obs['percent.ribo'].head()}")
    logger.info(f"前5行 percent.hb:\n{adata.obs['percent.hb'].head()}")

    # 绘制 QC 图
    sc.pl.violin(adata, ['nFeature_RNA', 'nCount_RNA', 'percent.mt', 'percent.ribo', 'percent.hb'],
                 save=f"{figures_dir}/qc_plots.png", show=False)
    logger.info(f"QC 图保存到: {figures_dir}/qc_plots.png")

    # QC 过滤函数
    def qc_filter(adata, qc_params):
        logger.info("应用 QC 过滤条件")
        adata = adata[
            (adata.obs['nFeature_RNA'] < qc_params['max_nFeature_RNA']) &
            (adata.obs['nFeature_RNA'] > qc_params['min_nFeature_RNA']) &
            (adata.obs['nCount_RNA'] < qc_params['max_nCount_RNA']) &
            (adata.obs['nCount_RNA'] > qc_params['min_nCount_RNA']) &
            (adata.obs['percent.mt'] < qc_params['max_percent_mt']) &
            (adata.obs['percent.ribo'] < qc_params['max_percent_ribo']) &
            (adata.obs['percent.hb'] < qc_params['max_percent_hb'])
        ]
        logger.info(f"过滤后的数据包含 {adata.n_obs} 行和 {adata.n_vars} 列")
        return adata

    # 应用 QC 过滤
    adata_filtered = qc_filter(adata, qc_params)

    # 保存过滤后的 AnnData 对象
    adata_filtered.write_h5ad(output_file)
    logger.info(f"过滤后的 AnnData 对象保存到: {output_file}")

except Exception as e:
    # 捕获错误并记录错误信息
    logger.error(f"发生错误: {str(e)}")
    raise
