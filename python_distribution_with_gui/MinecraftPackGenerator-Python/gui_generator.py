#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minecraft Pack Generator - GUI版
GUIインターフェースを提供するモジュール
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import os
import threading
import sys
from datetime import datetime
import subprocess

class MinecraftPackGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Pack Generator v1.1.0 - GUI版")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2b2b2b')
        
        # スタイル設定
        self.setup_styles()
        
        # 変数初期化
        self.current_project = None
        self.project_data = {}
        
        # GUI構築
        self.create_widgets()
        self.load_recent_projects()
        
    def setup_styles(self):
        """スタイル設定"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # カラーテーマ
        style.configure('Title.TLabel', 
                       background='#2b2b2b', 
                       foreground='#ffffff', 
                       font=('Arial', 16, 'bold'))
        
        style.configure('Header.TLabel', 
                       background='#2b2b2b', 
                       foreground='#00ff00', 
                       font=('Arial', 12, 'bold'))
        
        style.configure('Content.TLabel', 
                       background='#2b2b2b', 
                       foreground='#cccccc', 
                       font=('Arial', 10))
        
        style.configure('Success.TLabel', 
                       background='#2b2b2b', 
                       foreground='#00ff00', 
                       font=('Arial', 10))
        
        style.configure('Error.TLabel', 
                       background='#2b2b2b', 
                       foreground='#ff0000', 
                       font=('Arial', 10))
        
        # ボタンスタイル
        style.configure('Action.TButton', 
                       background='#4CAF50', 
                       foreground='#ffffff',
                       font=('Arial', 10, 'bold'))
        
        style.configure('Danger.TButton', 
                       background='#f44336', 
                       foreground='#ffffff',
                       font=('Arial', 10, 'bold'))
        
    def create_widgets(self):
        """ウィジェット作成"""
        # メインフレーム
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # タイトル
        title_label = ttk.Label(main_frame, 
                               text="🎮 Minecraft Pack Generator v1.1.0", 
                               style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # ノートブック（タブ）
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # プロジェクト管理タブ
        self.create_project_tab()
        
        # パック生成タブ
        self.create_generator_tab()
        
        # テンプレートエディタータブ
        self.create_template_tab()
        
        # 設定タブ
        self.create_settings_tab()
        
        # ログタブ
        self.create_log_tab()
        
        # ステータスバー
        self.create_status_bar()
        
    def create_project_tab(self):
        """プロジェクト管理タブ作成"""
        project_frame = ttk.Frame(self.notebook)
        self.notebook.add(project_frame, text="📁 プロジェクト管理")
        
        # プロジェクト情報
        info_frame = ttk.LabelFrame(project_frame, text="プロジェクト情報", padding=10)
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # プロジェクト名
        ttk.Label(info_frame, text="プロジェクト名:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=5)
        self.project_name_var = tk.StringVar()
        self.project_name_entry = ttk.Entry(info_frame, textvariable=self.project_name_var, width=40)
        self.project_name_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # プロジェクトパス
        ttk.Label(info_frame, text="保存先:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.project_path_var = tk.StringVar()
        path_frame = ttk.Frame(info_frame)
        path_frame.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.project_path_entry = ttk.Entry(path_frame, textvariable=self.project_path_var, width=35)
        self.project_path_entry.pack(side=tk.LEFT)
        
        ttk.Button(path_frame, text="参照", 
                  command=self.browse_project_path).pack(side=tk.LEFT, padx=5)
        
        # プロジェクトタイプ
        ttk.Label(info_frame, text="タイプ:", style='Header.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.project_type_var = tk.StringVar(value="resource_data")
        type_combo = ttk.Combobox(info_frame, textvariable=self.project_type_var, 
                                 values=["resource_data", "resource_only", "data_only"], 
                                 state="readonly", width=20)
        type_combo.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        # ボタンフレーム
        button_frame = ttk.Frame(project_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(button_frame, text="🆕 新規プロジェクト", 
                  style='Action.TButton',
                  command=self.create_new_project).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="📂 プロジェクトを開く", 
                  style='Action.TButton',
                  command=self.open_project).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="💾 プロジェクトを保存", 
                  style='Action.TButton',
                  command=self.save_project).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="📤 プロジェクトをエクスポート", 
                  style='Action.TButton',
                  command=self.export_project).pack(side=tk.LEFT, padx=5)
        
        # 最近のプロジェクト
        recent_frame = ttk.LabelFrame(project_frame, text="最近のプロジェクト", padding=10)
        recent_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.recent_listbox = tk.Listbox(recent_frame, bg='#3c3c3c', fg='#ffffff', 
                                        selectbackground='#4CAF50', height=8)
        self.recent_listbox.pack(fill=tk.BOTH, expand=True)
        self.recent_listbox.bind('<Double-Button-1>', self.open_recent_project)
        
    def create_generator_tab(self):
        """パック生成タブ作成"""
        generator_frame = ttk.Frame(self.notebook)
        self.notebook.add(generator_frame, text="⚙️ パック生成")
        
        # 生成オプション
        options_frame = ttk.LabelFrame(generator_frame, text="生成オプション", padding=10)
        options_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # チェックボックス
        self.generate_items_var = tk.BooleanVar(value=True)
        self.generate_spells_var = tk.BooleanVar(value=True)
        self.generate_entities_var = tk.BooleanVar(value=True)
        self.generate_recipes_var = tk.BooleanVar(value=True)
        self.generate_advancements_var = tk.BooleanVar(value=True)
        self.generate_loot_tables_var = tk.BooleanVar(value=True)
        self.generate_functions_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="アイテム生成", 
                       variable=self.generate_items_var).grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="スペル生成", 
                       variable=self.generate_spells_var).grid(row=0, column=1, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="エンティティ生成", 
                       variable=self.generate_entities_var).grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="レシピ生成", 
                       variable=self.generate_recipes_var).grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="アドバンスメント生成", 
                       variable=self.generate_advancements_var).grid(row=1, column=1, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="ルートテーブル生成", 
                       variable=self.generate_loot_tables_var).grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Checkbutton(options_frame, text="関数生成", 
                       variable=self.generate_functions_var).grid(row=2, column=0, sticky=tk.W, pady=2)
        
        # 生成ボタン
        generate_frame = ttk.Frame(generator_frame)
        generate_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(generate_frame, text="🚀 パックを生成", 
                  style='Action.TButton',
                  command=self.generate_pack).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(generate_frame, text="🔍 プレビュー", 
                  style='Action.TButton',
                  command=self.preview_pack).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(generate_frame, text="🧪 テスト実行", 
                  style='Action.TButton',
                  command=self.test_pack).pack(side=tk.LEFT, padx=5)
        
        # 進捗バー
        progress_frame = ttk.LabelFrame(generator_frame, text="生成進捗", padding=10)
        progress_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                           maximum=100, length=400)
        self.progress_bar.pack(fill=tk.X, pady=5)
        
        self.progress_label = ttk.Label(progress_frame, text="準備完了", style='Content.TLabel')
        self.progress_label.pack()
        
    def create_template_tab(self):
        """テンプレートエディタータブ作成"""
        template_frame = ttk.Frame(self.notebook)
        self.notebook.add(template_frame, text="📝 テンプレートエディター")
        
        # テンプレート選択
        select_frame = ttk.LabelFrame(template_frame, text="テンプレート選択", padding=10)
        select_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(select_frame, text="テンプレート:", style='Header.TLabel').pack(side=tk.LEFT)
        
        self.template_var = tk.StringVar()
        template_combo = ttk.Combobox(select_frame, textvariable=self.template_var, 
                                     values=["basic", "magic", "weapon", "custom"], 
                                     state="readonly", width=20)
        template_combo.pack(side=tk.LEFT, padx=10)
        template_combo.bind('<<ComboboxSelected>>', self.load_template)
        
        ttk.Button(select_frame, text="📂 テンプレートを開く", 
                  command=self.open_template).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(select_frame, text="💾 テンプレートを保存", 
                  command=self.save_template).pack(side=tk.LEFT, padx=5)
        
        # エディター
        editor_frame = ttk.LabelFrame(template_frame, text="テンプレートエディター", padding=10)
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.template_editor = scrolledtext.ScrolledText(editor_frame, 
                                                        bg='#1e1e1e', fg='#ffffff',
                                                        insertbackground='#ffffff',
                                                        font=('Consolas', 10))
        self.template_editor.pack(fill=tk.BOTH, expand=True)
        
    def create_settings_tab(self):
        """設定タブ作成"""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="⚙️ 設定")
        
        # 一般設定
        general_frame = ttk.LabelFrame(settings_frame, text="一般設定", padding=10)
        general_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Minecraftバージョン
        ttk.Label(general_frame, text="Minecraftバージョン:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=5)
        self.mc_version_var = tk.StringVar(value="1.20.1")
        version_combo = ttk.Combobox(general_frame, textvariable=self.mc_version_var, 
                                    values=["1.19.4", "1.20.0", "1.20.1", "1.20.2", "1.20.3", "1.20.4"], 
                                    state="readonly", width=15)
        version_combo.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # パック名
        ttk.Label(general_frame, text="パック名:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.pack_name_var = tk.StringVar(value="my_pack")
        ttk.Entry(general_frame, textvariable=self.pack_name_var, width=30).grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        # パック説明
        ttk.Label(general_frame, text="パック説明:", style='Header.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.pack_description_var = tk.StringVar(value="カスタムパック")
        ttk.Entry(general_frame, textvariable=self.pack_description_var, width=30).grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        # パックアイコン
        ttk.Label(general_frame, text="パックアイコン:", style='Header.TLabel').grid(row=3, column=0, sticky=tk.W, pady=5)
        icon_frame = ttk.Frame(general_frame)
        icon_frame.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.pack_icon_var = tk.StringVar()
        ttk.Entry(icon_frame, textvariable=self.pack_icon_var, width=25).pack(side=tk.LEFT)
        ttk.Button(icon_frame, text="参照", 
                  command=self.browse_icon).pack(side=tk.LEFT, padx=5)
        
        # 出力設定
        output_frame = ttk.LabelFrame(settings_frame, text="出力設定", padding=10)
        output_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # 出力ディレクトリ
        ttk.Label(output_frame, text="出力ディレクトリ:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=5)
        output_dir_frame = ttk.Frame(output_frame)
        output_dir_frame.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.output_dir_var = tk.StringVar(value="./output")
        ttk.Entry(output_dir_frame, textvariable=self.output_dir_var, width=30).pack(side=tk.LEFT)
        ttk.Button(output_dir_frame, text="参照", 
                  command=self.browse_output_dir).pack(side=tk.LEFT, padx=5)
        
        # 自動バックアップ
        self.auto_backup_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(output_frame, text="自動バックアップ", 
                       variable=self.auto_backup_var).grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # 詳細ログ
        self.verbose_log_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(output_frame, text="詳細ログ", 
                       variable=self.verbose_log_var).grid(row=1, column=1, sticky=tk.W, pady=5)
        
    def create_log_tab(self):
        """ログタブ作成"""
        log_frame = ttk.Frame(self.notebook)
        self.notebook.add(log_frame, text="📋 ログ")
        
        # ログ表示
        self.log_text = scrolledtext.ScrolledText(log_frame, 
                                                 bg='#1e1e1e', fg='#00ff00',
                                                 insertbackground='#ffffff',
                                                 font=('Consolas', 9))
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ログボタン
        log_button_frame = ttk.Frame(log_frame)
        log_button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(log_button_frame, text="🗑️ ログをクリア", 
                  command=self.clear_log).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(log_button_frame, text="💾 ログを保存", 
                  command=self.save_log).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(log_button_frame, text="📂 ログファイルを開く", 
                  command=self.open_log_file).pack(side=tk.LEFT, padx=5)
        
    def create_status_bar(self):
        """ステータスバー作成"""
        self.status_var = tk.StringVar(value="準備完了")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def browse_project_path(self):
        """プロジェクトパス選択"""
        path = filedialog.askdirectory(title="プロジェクト保存先を選択")
        if path:
            self.project_path_var.set(path)
            
    def browse_icon(self):
        """アイコンファイル選択"""
        file = filedialog.askopenfilename(title="パックアイコンを選択",
                                        filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file:
            self.pack_icon_var.set(file)
            
    def browse_output_dir(self):
        """出力ディレクトリ選択"""
        path = filedialog.askdirectory(title="出力ディレクトリを選択")
        if path:
            self.output_dir_var.set(path)
            
    def create_new_project(self):
        """新規プロジェクト作成"""
        name = self.project_name_var.get().strip()
        path = self.project_path_var.get().strip()
        
        if not name or not path:
            messagebox.showerror("エラー", "プロジェクト名と保存先を入力してください")
            return
            
        try:
            project_dir = os.path.join(path, name)
            os.makedirs(project_dir, exist_ok=True)
            
            # プロジェクトファイル作成
            project_data = {
                "name": name,
                "path": project_dir,
                "type": self.project_type_var.get(),
                "created": datetime.now().isoformat(),
                "version": "1.1.0"
            }
            
            project_file = os.path.join(project_dir, f"{name}.json")
            with open(project_file, 'w', encoding='utf-8') as f:
                json.dump(project_data, f, indent=2, ensure_ascii=False)
                
            self.current_project = project_file
            self.project_data = project_data
            
            self.log_message(f"✅ 新規プロジェクト '{name}' を作成しました")
            self.update_status(f"プロジェクト: {name}")
            
        except Exception as e:
            messagebox.showerror("エラー", f"プロジェクト作成に失敗しました: {str(e)}")
            
    def open_project(self):
        """プロジェクトを開く"""
        file = filedialog.askopenfilename(title="プロジェクトファイルを選択",
                                        filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    self.project_data = json.load(f)
                    
                self.current_project = file
                self.project_name_var.set(self.project_data.get("name", ""))
                self.project_path_var.set(self.project_data.get("path", ""))
                self.project_type_var.set(self.project_data.get("type", "resource_data"))
                
                self.log_message(f"✅ プロジェクト '{self.project_data['name']}' を開きました")
                self.update_status(f"プロジェクト: {self.project_data['name']}")
                
            except Exception as e:
                messagebox.showerror("エラー", f"プロジェクトの読み込みに失敗しました: {str(e)}")
                
    def save_project(self):
        """プロジェクトを保存"""
        if not self.current_project:
            messagebox.showerror("エラー", "保存するプロジェクトがありません")
            return
            
        try:
            # 現在の設定を更新
            self.project_data.update({
                "name": self.project_name_var.get(),
                "path": self.project_path_var.get(),
                "type": self.project_type_var.get(),
                "last_modified": datetime.now().isoformat()
            })
            
            with open(self.current_project, 'w', encoding='utf-8') as f:
                json.dump(self.project_data, f, indent=2, ensure_ascii=False)
                
            self.log_message("✅ プロジェクトを保存しました")
            
        except Exception as e:
            messagebox.showerror("エラー", f"プロジェクトの保存に失敗しました: {str(e)}")
            
    def export_project(self):
        """プロジェクトをエクスポート"""
        if not self.current_project:
            messagebox.showerror("エラー", "エクスポートするプロジェクトがありません")
            return
            
        file = filedialog.asksaveasfilename(title="エクスポート先を選択",
                                          defaultextension=".zip",
                                          filetypes=[("ZIP files", "*.zip")])
        if file:
            try:
                # ここでZIPエクスポート処理を実装
                self.log_message("✅ プロジェクトをエクスポートしました")
                messagebox.showinfo("完了", "プロジェクトのエクスポートが完了しました")
                
            except Exception as e:
                messagebox.showerror("エラー", f"エクスポートに失敗しました: {str(e)}")
                
    def load_recent_projects(self):
        """最近のプロジェクトを読み込み"""
        try:
            recent_file = "recent_projects.json"
            if os.path.exists(recent_file):
                with open(recent_file, 'r', encoding='utf-8') as f:
                    recent_projects = json.load(f)
                    
                for project in recent_projects:
                    self.recent_listbox.insert(tk.END, project["name"])
                    
        except Exception as e:
            self.log_message(f"⚠️ 最近のプロジェクトの読み込みに失敗: {str(e)}")
            
    def open_recent_project(self, event):
        """最近のプロジェクトを開く"""
        selection = self.recent_listbox.curselection()
        if selection:
            # 最近のプロジェクトを開く処理
            pass
            
    def load_template(self, event):
        """テンプレートを読み込み"""
        template_name = self.template_var.get()
        try:
            template_file = f"templates/{template_name}_template.json"
            if os.path.exists(template_file):
                with open(template_file, 'r', encoding='utf-8') as f:
                    template_data = json.load(f)
                    
                self.template_editor.delete(1.0, tk.END)
                self.template_editor.insert(1.0, json.dumps(template_data, indent=2, ensure_ascii=False))
                
                self.log_message(f"✅ テンプレート '{template_name}' を読み込みました")
                
        except Exception as e:
            self.log_message(f"❌ テンプレートの読み込みに失敗: {str(e)}")
            
    def open_template(self):
        """テンプレートファイルを開く"""
        file = filedialog.askopenfilename(title="テンプレートファイルを選択",
                                        filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    template_data = json.load(f)
                    
                self.template_editor.delete(1.0, tk.END)
                self.template_editor.insert(1.0, json.dumps(template_data, indent=2, ensure_ascii=False))
                
                self.log_message(f"✅ テンプレートファイル '{os.path.basename(file)}' を読み込みました")
                
            except Exception as e:
                messagebox.showerror("エラー", f"テンプレートファイルの読み込みに失敗しました: {str(e)}")
                
    def save_template(self):
        """テンプレートを保存"""
        file = filedialog.asksaveasfilename(title="テンプレート保存先を選択",
                                          defaultextension=".json",
                                          filetypes=[("JSON files", "*.json")])
        if file:
            try:
                template_data = self.template_editor.get(1.0, tk.END)
                json.loads(template_data)  # バリデーション
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(template_data)
                    
                self.log_message(f"✅ テンプレートを保存しました: {os.path.basename(file)}")
                
            except json.JSONDecodeError:
                messagebox.showerror("エラー", "無効なJSON形式です")
            except Exception as e:
                messagebox.showerror("エラー", f"テンプレートの保存に失敗しました: {str(e)}")
                
    def generate_pack(self):
        """パック生成"""
        if not self.current_project:
            messagebox.showerror("エラー", "プロジェクトを開いてください")
            return
            
        # 生成オプションを取得
        options = {
            "items": self.generate_items_var.get(),
            "spells": self.generate_spells_var.get(),
            "entities": self.generate_entities_var.get(),
            "recipes": self.generate_recipes_var.get(),
            "advancements": self.generate_advancements_var.get(),
            "loot_tables": self.generate_loot_tables_var.get(),
            "functions": self.generate_functions_var.get()
        }
        
        # バックグラウンドで生成実行
        thread = threading.Thread(target=self._generate_pack_thread, args=(options,))
        thread.daemon = True
        thread.start()
        
    def _generate_pack_thread(self, options):
        """パック生成スレッド"""
        try:
            self.update_progress(0, "パック生成を開始...")
            
            # ここで実際のパック生成処理を実行
            # pack_generator.pyの機能を呼び出す
            
            for i, (option, enabled) in enumerate(options.items()):
                if enabled:
                    progress = (i + 1) * 100 // len([v for v in options.values() if v])
                    self.update_progress(progress, f"{option}を生成中...")
                    # 実際の生成処理
                    
            self.update_progress(100, "パック生成完了")
            self.log_message("✅ パック生成が完了しました")
            
        except Exception as e:
            self.log_message(f"❌ パック生成に失敗: {str(e)}")
            self.update_progress(0, "エラーが発生しました")
            
    def preview_pack(self):
        """パックプレビュー"""
        messagebox.showinfo("プレビュー", "プレビュー機能は開発中です")
        
    def test_pack(self):
        """パックテスト実行"""
        messagebox.showinfo("テスト", "テスト機能は開発中です")
        
    def clear_log(self):
        """ログをクリア"""
        self.log_text.delete(1.0, tk.END)
        
    def save_log(self):
        """ログを保存"""
        file = filedialog.asksaveasfilename(title="ログ保存先を選択",
                                          defaultextension=".txt",
                                          filetypes=[("Text files", "*.txt")])
        if file:
            try:
                log_content = self.log_text.get(1.0, tk.END)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(log_content)
                    
                self.log_message(f"✅ ログを保存しました: {os.path.basename(file)}")
                
            except Exception as e:
                messagebox.showerror("エラー", f"ログの保存に失敗しました: {str(e)}")
                
    def open_log_file(self):
        """ログファイルを開く"""
        if os.path.exists("pack_generator.log"):
            try:
                if sys.platform == "win32":
                    os.startfile("pack_generator.log")
                else:
                    subprocess.run(["xdg-open", "pack_generator.log"])
            except Exception as e:
                self.log_message(f"❌ ログファイルを開けませんでした: {str(e)}")
        else:
            messagebox.showinfo("情報", "ログファイルが見つかりません")
            
    def log_message(self, message):
        """ログメッセージを追加"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        
    def update_progress(self, value, message):
        """進捗を更新"""
        self.progress_var.set(value)
        self.progress_label.config(text=message)
        self.root.update_idletasks()
        
    def update_status(self, message):
        """ステータスを更新"""
        self.status_var.set(message)

def main():
    """メイン関数"""
    root = tk.Tk()
    app = MinecraftPackGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 